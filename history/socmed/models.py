from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from flask_sqlalchemy.model import Model
from history.mixins import TimeStampMixin
from history import db


class PostModel(TimeStampMixin, db.Model):
    __tablename__ = 'post' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_c = db.relationship('PostComment', backref='post', lazy=True)
    title =  Column(String(256), nullable=False)
    category = Column(String, nullable=False) # should have choices 



    """
    Question, Trivia, Help me study, Philippines, Unrelated
    """



    def __repr__(self) -> str:
        return self.title
    

class PostComment(TimeStampMixin, db.Model):
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    comment = Column(String(256), nullable=False)

    def __repr__(self) -> str:
        return str(self.comment).title()
    

# PostModel.__table__.create(db.session.bind)
# # PostComment.__table__.create(db.session.bind)