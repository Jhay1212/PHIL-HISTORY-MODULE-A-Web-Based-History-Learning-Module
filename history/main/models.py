from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, LargeBinary, Boolean
from datetime import datetime
from history import db
from flask_ckeditor import CKEditorField
from history.mixins import TimeStampMixin

class Unit(TimeStampMixin, db.Model):
    id = Column(Integer, primary_key=True)
    lesson_key = db.relationship("Lesson", backref='unit', lazy=True)
    unit_title = Column(String(64), nullable=False)
    description = Column(String(56), nullable=False, default='Description')

class Lesson(TimeStampMixin, db.Model):
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey('unit.id'), nullable=False)
    title = Column(String(120), nullable=False, default='Lesson Title')
    content = Column(Text(), nullable=False)
    comments = db.relationship('Comment', backref='lesson', lazy=True)
    mini_notes = db.relationship('MiniNotes', backref='lesson', lazy=True)
    bookmark = db.relationship('BookMark', backref='title', lazy=True)
    
    # def __init__(self) -> None:
        # Lesson.unit_id = 1
    def __str__(self) -> str:
        return self.title
    
class MiniNotes(TimeStampMixin, db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False, default="Tite")
    notes = Column(Text(), nullable=False)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    # date_posted = Column(DateTime(), nullable=False, default=datetime.now())
    # date_updated = Column(DateTime(), nullable=False, onupdate=datetime.now, default=datetime.now())
    # submit = Sub

    def __repr__(self) -> str:
        return self.notes

class Comment(TimeStampMixin, db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    comment = Column(String(128), nullable=False)
    # date_posted = Column(DateTime(), default=datetime.now(), nullable=False)
    # date_edited = Column(DateTime(), default=datetime.now(), nullable=False)
    
    def __str__(self):
        return self.comment[:20].title()


class BookMark(TimeStampMixin, db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    lesson_id = Column(Integer, ForeignKey('lesson.id'), nullable=False)


class Hero(db.Model):
    # __tablename__ = 'hero'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    # profile_pic = Column/(LargeBinary(), nullable=False, default='Pic')
    bio = Column(String(), nullable=False)
    contribution = Column(Text, nullable=False)

    def __str__(self) -> str:
        return self.name
    
class President(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    # profile_pic = Column/(LargeBinary(), nullable=False, default='Pic')
    bio = Column(String(), nullable=False)
    contribution = Column(Text, nullable=False)

# class PreTestQuiz(db.Model):
#     id = Column(Integer, primary_key=True)
#     question_id = Column(Integer, ForeignKey('question.id'), nullable=False)

#     # question = Column(String(128), nullable=False)


# class PreTestQuestion(db.Model):
#     id = Column(Integer, primary_key=True)
#     question_id = db.relationship('Question', backref='question', lazy=True)
#     # question_type = Column(Boolean, default=True)
#     question = Column(String(128), nullable=False)
#     choices = 'something'

# class PostTestQuiz(db.Model):
#     id = Column(Integer, primary_key=True)
#     question_id = Column(Integer, ForeignKey('question.id'), nullable=False)
#     # how to implement which answer is correct for the ``