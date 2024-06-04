from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt

from flask_mail import Mail

from flask_pagedown import PageDown 
from flask_ckeditor import CKEditor

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from os import environ
# App setup and configuration

db = SQLAlchemy()
login_manager = LoginManager()
bcrpyt = Bcrypt()
pagedown = PageDown()
mail_manager = Mail()

ckeditor = CKEditor()

def create_app():

    app = Flask('__main__')
    app.config['SECRET_KEY'] = environ.get("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['FLASK_ADMIN_SWATCH'] = 'flatly'
    app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
    db.init_app(app)
    app.app_context().push()
    pagedown.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = environ.get("MAIL_USERNAME")
    app.config['MAIL_PASSWORD'] = environ.get("MAIL_PASSWORD")
    mail_manager.init_app(app)

    from history.main.models import BookMark, Lesson, MiniNotes, Hero, President
    from history.auth.models import User
    from history.auth.routes import acc
    from history.main.routes import main
    from history.chatbot.routes import cbot
    app.register_blueprint(acc)
    app.register_blueprint(main)
    app.register_blueprint(cbot)



    admin = Admin(app)
    class MiniNotesModelView(ModelView):
        def is_accesible(self):
            return current_user.is_authenticated
        
    admin.add_view(ModelView(MiniNotes, db.session))
    admin.add_view(ModelView(Hero, db.session))
    admin.add_view(ModelView(President, db.session))
    admin.add_view(ModelView(Lesson, db.session))
    admin.add_view(ModelView(BookMark, db.session))
    admin.add_view(ModelView(User, db.session))


    # class 

    return app
# from . import routers
