from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for
from .forms import NotesForm
from .models import MiniNotes
from history import db
main = Blueprint('/', __name__, template_folder='templates')

@main.route('/home', methods=['GET', 'POST'])
def home():

    return render_template('home.html')


@main.route('/lesson', methods=['POST', 'GET'])
def lesson():
    forms = NotesForm()
    if forms.validate_on_submit():
        notes = MiniNotes(notes=forms.notes.data)
        print(forms.notes.data)
        db.session.add(notes)
        db.session.commit()
    print(forms.errors)
    return render_template('lsson.html', forms=forms)

@main.route('/')
def homepage():
    return redirect('home')


@main.route('/view/notes')
def view():
    notes = MiniNotes.query.all()
    print(notes)
    return render_template('notes.html', notes=notes)