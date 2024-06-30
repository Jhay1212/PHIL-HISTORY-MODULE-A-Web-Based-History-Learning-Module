from wtforms import StringField, SubmitField, SelectField, EmailField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo


CATEGORY_CHOICES = [('Question', 'Q'), ('Trivia', 'T')]

class PostForm(FlaskForm):
    title = StringField("Enter Post", validators=[DataRequired(), Length(min=2, max=256)])
    link = StringField("Paste a link")
    category = SelectField('Select a category', validators=[DataRequired()], choices=[CATEGORY_CHOICES])
    submit = SubmitField('Post')

class EditUserForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=16)])
    email = EmailField('Email', validators=[Length(min=4, max=256)])
    new_password = PasswordField('Password', validators=[Length(min=6)])
    new_confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Signup')