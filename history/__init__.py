from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_pagedown import PageDown
from flask_mail import Mail
# App setup and configuration

db = SQLAlchemy()
login_manager = LoginManager()
bcrpyt = Bcrypt()
pagedown = PageDown()
mail_manager = Mail()



def create_app():

    app = Flask('__main__', template_folder='history/templates')
    app.config['SECRET_KEY'] = '54bfcdc4c1d2711a765a55c7cfdca7dc360da1819d188cfd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    app.app_context().push()
    pagedown.init_app(app)
    login_manager.init_app(app)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'rjhay1070@gmail.com'
    app.config['MAIL_PASSWORD'] = 'ifwx zmrg pqin ysiz '
    mail_manager.init_app(app)

    from history.auth.routes import acc
    from history.main.routes import main
    app.register_blueprint(acc)
    app.register_blueprint(main)

    return app
# from . import routers
