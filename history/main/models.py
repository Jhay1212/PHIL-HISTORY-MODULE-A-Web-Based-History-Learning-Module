from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from datetime import datetime
from history import db
from flask_ckeditor import CKEditorField

class Lesson(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False, default='Lesson Title')
    content = Column(Text(), nullable=False)
    mini_notes = db.relationship('MiniNotes', backref='lesson', lazy=True)

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


    def __repr__(self) -> str:
        return self.notes