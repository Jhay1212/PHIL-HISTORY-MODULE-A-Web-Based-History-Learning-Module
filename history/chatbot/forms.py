from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class Chatbot(FlaskForm):
    chat = StringField('Chat', validators=[DataRequired()])
    submit = SubmitField('Send')