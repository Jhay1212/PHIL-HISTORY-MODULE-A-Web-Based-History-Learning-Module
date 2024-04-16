from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, request, jsonify
from .forms import NotesForm
from .models import MiniNotes
from history import db
from googletrans import Translator

translator = Translator()
main = Blueprint('/', __name__, template_folder='templates', static_folder='static')

@main.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home/home.html')


@main.route('/lesson', methods=['POST', 'GET'])
def lesson():
    forms = NotesForm()
    if forms.validate_on_submit():
        notes = MiniNotes(notes=forms.notes.data)
        print(forms.notes.data)
        db.session.add(notes)
        db.session.commit()
    print(forms.errors)
    return render_template('lessons/unit1/lesson1.html', forms=forms)

@main.route('/home')
def homepage():
    return redirect('/')

@main.route('/base')
def base():
    return render_template('base.html')

@main.route('/view/notes')
def view():
    notes = MiniNotes.query.all()
    print(notes)
    return render_template('notes.html', notes=notes)


@main.route('/gallery')
def gallery():
    return render_template('gallery.html')



@main.route('/quiz')
def quiz():
    return render_template('QUIZ1/quiz.html')



@main.route('/chat', methods=['POST', 'GHOST'])
def chatbot():
    msg = request.form['msg']
    print(get_response_chatbot('ano ba ang ginagawa ko ngayon'))
    return render_template('chat.html')

def get_response_chatbot(txt):
    response = translator.translate(txt)
    return response