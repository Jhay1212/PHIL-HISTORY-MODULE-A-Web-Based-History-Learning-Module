from flask import Flask, request, session, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeSerializer
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt

from flask_mail import Mail

from flask_pagedown import PageDown 
from flask_ckeditor import CKEditor

from flask_admin import Admin
# from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView
import os 
# App setup and configuration

BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASEDIR, 'uploads')
db = SQLAlchemy()
login_manager = LoginManager()
bcrpyt = Bcrypt()
pagedown = PageDown()
mail_manager = Mail()

ckeditor = CKEditor()

def create_app():
    print(BASEDIR)

    app = Flask('__main__')
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' or os.path.join(BASEDIR, 'site.db')
    app.config['FLASK_ADMIN_SWATCH'] = 'flatly'
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    db.init_app(app)
    # migrate = Migrate(app, db)
    app.app_context().push()
    pagedown.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    mail_manager.init_app(app)
    serializer = URLSafeSerializer(app.config['SECRET_KEY'])

    from history.main.models import BookMark, Lesson, MiniNotes, Hero, President, Unit
    from history.auth.models import User
    from history.socmed.models import PostComment, PostModel
    from history.auth.routes import acc
    from history.main.routes import main
    from history.chatbot.routes import cbot
    from history.socmed.routes import socmed
    """" Registering blueprint of different modular part"""

    app.register_blueprint(acc)
    app.register_blueprint(main)
    app.register_blueprint(cbot)
    app.register_blueprint(socmed)

    @app.after_request
    def save_response(r):
        
        """
        Save the response of the request to the session history.

        This function is a Flask after_request hook that saves the response of the request to the session history.
        It checks if the request method is 'POST' or if the endpoint is 'static', in which case it returns the response as is.
        Otherwise, it appends the endpoint, view arguments, and status code of the response to the session history.
        The session history is limited to the last 5 entries.

        Parameters:
            r (Response): The response object of the request.

        Returns:
            Response: The response object of the request.
        """
        if request.method == 'POST':
            return r
        if request.endpoint == 'static':
            return r
        
        history = session.get('history', [])
        if history:
            if history[-1][0] == request.endpoint and history[-1][1] == request.view_args:
                return r

        history.append([
            request.endpoint,
            request.view_args,
            r.status_code
        ])
        session['history'] = history[-5:]
        return r 

    print(app._static_folder)
    admin = Admin(app)
    class MiniNotesModelView(ModelView):
        def is_accesible(self):
            return current_user.is_authenticated
    class LessonModelView(ModelView):
        column_display_pk = True
        column_hide_backrefs = False
        # column_display_all_relations = True
        column_list = ('title', 'content', 'unit')
        form_list = ('title', 'content', 'units')
        
    admin.add_view(ModelView(MiniNotes, db.session))
    admin.add_view(ModelView(Unit, db.session))
    admin.add_view(ModelView(PostModel, db.session))
    admin.add_view(ModelView(PostComment, db.session))
    admin.add_view(ModelView(Hero, db.session))
    admin.add_view(ModelView(President, db.session))
    admin.add_view(LessonModelView(Lesson, db.session))
    print('lesson model view added to admin')
    admin.add_view(ModelView(BookMark, db.session))
    admin.add_view(ModelView(User, db.session))


    # class 

    # DB INITIALIZATION

    
    with app.app_context():
        # db.drop_all()
        db.create_all()

    return app
# from . import routers


def url_back(fallback='/.home', *args, **kwargs):
    for step in session.get('history', [][::-1]):
        if step[0] == request.endpoint and step[1] == request.view_args:
            continue
        if 200 <= step[2] < 300:
            return url_for(step[0], **step[1]) 
        
        print(fallback)
    return url_back(fallback, *args, **kwargs)