from flask.blueprints import Blueprint
from flask_login import current_user
from flask import render_template, redirect, url_for, request, jsonify
from .forms import NotesForm, ChatForm, PreTestForm
from history.auth.models import User
from .models import MiniNotes, Comment
from history import db
# from .utils import convo
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
        print(lesson)
        return redirect(url_for('/.lesson'))
    print(forms.errors)
    return render_template('lessons/unit1/lesson1.html', forms=forms)

@main.route('/home')
def homepage():
    return redirect('/')

@main.route('/base')
def base():
    return render_template('base.html')

@main.route('/view/notes/<int:pk>')
def view(pk):
    user = User.query.get(pk)
    # user = db.session.execute(db.select(User).get(pk)).scalar_one()
    notes = MiniNotes.query.all()
    print(notes)
    return render_template('notes/notes.html', notes=notes, user=user)


@main.route('/gallery')
def gallery():
    return render_template('gallery/gallery.html')

@main.route('/event/<string:event>')
def event_view(event):
    return render_template('event/event.html')

@main.route('/quiz')
def quiz():
    return render_template('QUIZ1/quiz.html')


@main.route('/pretest/<int:unit>/<int:lesson>', methods=['GET', 'POST'])
def pre_test(unit, lesson):
    forms = PreTestForm()
    if forms.validate_on_submit():
        return redirect(url_for('/.view'))
    return render_template('QUIZ1/pretest.html', unit=unit, lesson=lesson, forms=forms)
    


@main.route('/post-test/unit/<int:unit>/lesson/<int:lesson>')
def post_test(unit, lesson):
    return render_template('QUIZ1/posttest.html', unit=unit, lesson=lesson)



@main.route('/chronohistory', methods=['POST', 'GET'])
def choronoh():
    return render_template('games/chronoh.html')
# @main.route('/chat', methods=["POST", 'GET'])
# def chatbot_view():
#     forms = ChatForm()
#     if forms.validate_on_submit():
#         mess = forms.text.data
#         convo.send_message(mess)
#         response = convo.last.text
#         print(response[3:])
#         return render_template('chatbot/chatbot.html', response=response, forms=forms)
#     response = convo.last.text
#     print(forms.errors)
#     return render_template('chatbot/chatbot.html', response=response[4:], forms=forms)



@main.route('/timeline')
def timeline():
    return render_template('timeline/timeline.html')

def get_response_chatbot(txt):
    pass


@main.route('/heroes/')
def heroes():
    """
    List of all the heroes will be displayed here and when the use click
    on certain hero he will be redirected to that hero page

    Hero will either be get through api or database?
    """
    return render_template('hero/heroes.html')


@main.route('/hero/<int:pk>')
def hero(pk):
    """
    Single hero page
    """
    # hero = Hero.query.get(pk)
    print(hero)
    return render_template('hero/hero.html', hero='hero')


@main.route('/user/bookmark')
def bookmark():
    return render_template('bookmark/bookmark.html')
    
@main.route('/president/<string:name>')
def president(name):
    """
    Single page view of the president of the philippines
    """
    return render_template('president/president.html', hero='name')


@main.route('/history/quest')
def pquest():
    return render_template('game/quest.html')
def chatbot():
    msg = request.form['msg']
    print(get_response_chatbot('ano ba ang ginagawa ko ngayon'))
    return render_template('chat.html')

