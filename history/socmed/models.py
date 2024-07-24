from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from flask_sqlalchemy.model import Model
from history.mixins import TimeStampMixin
from history import db
from .utils import  chat_session, send_message
from sqlalchemy import event



post_category = db.Table(
    'post_category',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)
class Category(db.Model):
    id = Column(Integer, primary_key=True)
    # category = 

class PostModel(TimeStampMixin, db.Model):
    __tablename__ = 'post' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_c = db.relationship('PostComment', backref='post', lazy=True)
    title =  Column(String(256), nullable=False)
    category = db.relationship('Category', secondary=post_category, backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self) -> str:
        return f'Post - {self.title}: Category: {self.category}'

    def save(self):
        db.session.add(self)
        db.session.commit()
        # try:

        #      comment = PostComment(post_id=self.id, comment=send_message(self.title))
        #      db.session.add(comment)
        #      db.session.commit()
        response = chat_session.send_message(self.title)
        # PostComment.__table__.create(db.session.bind)
        print(response.text)

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

def add_child_comment(mapper, connection, target):
    transaction = connection.begin()
    comment = PostComment(post_id=target.id, comment=send_message(target.title))
    db.session.add(comment)
    db.session.commit()

# event.listen(PostModel, 'after_insert', add_child_comment)