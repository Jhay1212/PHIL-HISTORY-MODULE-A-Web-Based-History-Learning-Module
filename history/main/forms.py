from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms.validators import Length, DataRequired, EqualTo,  ValidationError
from .models import Lesson, MiniNotes
from flask_ckeditor import CKEditorField
from wtforms.fields import (StringField, 
                            IntegerField, 
                            SubmitField, 
                            BooleanField, 
                            PasswordField, 
                            EmailField,
                            RadioField)


class NotesForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=256)])
    notes = CKEditorField("Enter Notes", validators=[DataRequired()])
    submit = SubmitField('Save')

    
    # def validate_not

class ChatForm(FlaskForm):
    text = StringField('Chat', validators=[DataRequired()])
    submit = SubmitField('Save')


class PreTestForm(FlaskForm):
    answer = RadioField('Choose an Answer', validators=[DataRequired()], choices=[('Who killed Jose Rizal?', "Joe"), ('something', 'anything here')])
    submit = SubmitField("Finish Test")

class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Search')