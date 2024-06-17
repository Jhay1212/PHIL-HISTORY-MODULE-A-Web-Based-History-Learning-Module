from flask_sqlalchemy import model
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime 
from sqlalchemy.ext.declarative import declared_attr
from history import db
class TimeStampMixin(object):
    date_created = Column(DateTime, default=datetime.now(), onupdate=datetime.now)

    def save(self):
        print(f'adding {self} to db')
        db.session.add(self)
        db.session.commit()
        print(f'Commited {self} into database')