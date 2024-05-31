from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, LargeBinary, Boolean
from datetime import datetime
from history import db
from flask_ckeditor import CKEditorField

class Lesson(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False, default='Lesson Title')
    content = Column(Text(), nullable=False)
    comments = db.relationship('Comment', backref='lesson', lazy=True)
    mini_notes = db.relationship('MiniNotes', backref='lesson', lazy=True)
    bookmark = db.relationship('BookMark', backref='title', lazy=True)
    
    def __str__(self) -> str:
        return self.title
    
class MiniNotes(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False, default="Tite")
    notes = Column(Text(), nullable=False)
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    date_posted = Column(DateTime(), nullable=False, default=datetime.now())
    date_updated = Column(DateTime(), nullable=False, onupdate=datetime.now, default=datetime.now())
    # submit = Sub

    def __repr__(self) -> str:
        return self.notes

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    comment = Column(String(128), nullable=False)
    date_posted = Column(DateTime(), default=datetime.now(), nullable=False)
    date_edited = Column(DateTime(), default=datetime.now(), nullable=False)
    
    def __str__(self):
        return self.comment[:20].title()


class BookMark(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    lesson_id = Column(Integer, ForeignKey('lesson.id'), nullable=False)


# class Hero(db.Model):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(256), nullable=False)
#     # profile_pic = Column/(LargeBinary(), nullable=False, default='Pic')
#     bio = Column(String(), nullable=False)


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
#     # how to implement which answer is correct for the 