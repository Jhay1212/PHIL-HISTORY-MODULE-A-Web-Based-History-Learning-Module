from flask import current_app
from history import db
from flask_sqlalchemy import model
from flask_login import UserMixin
from history import login_manager
from sqlalchemy import Integer, String, ForeignKey, DateTime, Column
from datetime import datetime
from itsdangerous import TimedSerializer as Serializer

# from flask_security import RoleMixin


# role_user = db.Table('role', 
#                     db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
#                     db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
#                     )


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = Column(String(256), unique=True, nullable=False)
    email = Column(String(256), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    bookmark = db.relationship('BookMark', backref='user', lazy=True)
    notes = db.relationship('MiniNotes', backref='user', lazy=True)
    
    def get_reset_token(self, expired_sec=18000):
        s = Serializer(current_app.config['SECRET_KEY'], expired_sec)
        return s.dumps({'user_id': self.id}).decode()

    def jhay(self):
        return self


    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        
        return User.query.get(user_id)
    
    def __str__(self) -> str:
        return str(self.username).title()
    


