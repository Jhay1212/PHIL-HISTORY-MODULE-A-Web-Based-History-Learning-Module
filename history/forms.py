from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo,  ValidationError


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=16), DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')


class LessonForm(FlaskForm):
    title = StringField('Title', validators=[Length(max=120), DataRequired()])
    content = PageDownField('Enter the Lesson', validators=[DataRequired()])


class NotesForm(FlaskForm):
    notes = PageDownField('Enter notes')
    

    def validate_notes(self, id):
        if self.notes == None:
            self.notes = id