from flask import current_app
from history import db
from flask_sqlalchemy import model
from flask_login import UserMixin
from history import login_manager
from sqlalchemy import Integer, String, ForeignKey, DateTime, Column
from datetime import datetime
from itsdangerous import TimedSerializer as Serializer

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = Column(String(256), unique=True, nullable=False)
    email = Column(String(256), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    notes = db.relationship('MiniNotes', backref='user', lazy=True)

    def get_reset_token(self, expired_sec=18000):
        s = Serializer(current_app.config['SECRET_KEY'], expired_sec)
        return s.dumps({'user_id': self.id}).decode()


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
    


class Lesson(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False, default='Lesson Title')
    content = Column(String(), nullable=False)
    mini_notes = db.relationship('MiniNotes', backref='lesson', lazy=True)

    def __str__(self) -> str:
        return self.title
    
class MiniNotes(db.Model):
    id = Column(Integer, primary_key=True)
    notes = Column(String(256))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    date_posted = Column(DateTime(), nullable=False, default=datetime.now())
    date_updated = Column(DateTime(), nullable=False, onupdate=datetime.now)

    def __repr__(self) -> str:
        return self.notes[:20]