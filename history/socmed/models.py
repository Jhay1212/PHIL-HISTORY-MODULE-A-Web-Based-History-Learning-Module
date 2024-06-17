from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from flask_sqlalchemy.model import Model
from history.mixins import TimeStampMixin
from history import db


class PostModel(TimeStampMixin, Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title =  Column(String(256), nullable=False)
    



    def __repr__(self) -> str:
        return self.title