from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms.fields import StringField, IntegerField, SubmitField, BooleanField, PasswordField, EmailField
from wtforms.validators import Length, DataRequired, EqualTo,  ValidationError
from .models import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=16), DataRequired()])
    email = EmailField('Email', validators=[Length(min=4, max=256), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email should be unique")
    
    
    # def validate_password(self, id):
    #     user = User.query.get(id)
    #     if len(user.password.data) < 8:
    #         raise ValidationError('Passowrd must be 8 characters long')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'nng-model': 'NameModel'})
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember', default=True)
    submit = SubmitField('Signin')

    # def validate_password(self, password):
    #     user = 

class RequestResetForm(FlaskForm):
    email = EmailField('Email', validators=[Length(min=4, max=256), DataRequired()])
    submit = SubmitField('Request Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No account with that email.')
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField("New Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[EqualTo('password'), DataRequired()])
    submit = SubmitField('Reset Password')    
        