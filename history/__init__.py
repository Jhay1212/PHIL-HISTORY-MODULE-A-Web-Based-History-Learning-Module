from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_pagedown import PageDown
from flask_mail import Mail
from flask_ckeditor import CKEditor
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
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
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

    from history.auth.routes import acc
    from history.main.routes import main
    from history.chatbot.routes import cbot
    app.register_blueprint(acc)
    app.register_blueprint(main)
    app.register_blueprint(cbot)


    return app
# from . import routers
from history import admin
# admin