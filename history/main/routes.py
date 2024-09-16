from flask.blueprints import Blueprint
from flask_login import current_user
from flask import (render_template, 
                   redirect, 
                   url_for, 
                   request, 
                   jsonify, 
                   send_file,
                   session,
                    g,
                    sessions,
                    get_flashed_messages)
from sqlalchemy import select, or_
from flask_sqlalchemy.session import Session
from flask_sqlalchemy.query import Query

import os, json

from .forms import NotesForm, PreTestForm, SearchForm, CommentForm
from .models import MiniNotes, Comment, Hero, President, Lesson, Unit, BookMark
from history.auth.models import User
from history import db

from history import BASEDIR

from .utils import search_google


# from .utils import convo
main = Blueprint('/', __name__, template_folder='templates', static_folder='static')
print(dir(current_user))
@main.before_app_request
def check_admin_auth():
    """
    A decorator function that checks if the current user is an admin before allowing access to the admin page.

    This function is decorated with `@main.before_app_request` which means it will be called before every request to the Flask app.

    Parameters:
        None

    Returns:
        None

    Raises:
        None

    Example Usage:
        @main.before_app_request
        def check_admin_auth():
            if request.path.startswith('/admin'):
                if current_user.username != 'admin':
                    return redirect(url_for('auth.login'))

    """
    if request.path.startswith('/admin'):
        if current_user.username != 'admin':
            return redirect(url_for('/.auth.login'))



@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', e=e), 404


@main.context_processor
def base():
    # pass the form to all the base template
    form = SearchForm()
    print(session)
    # g.searchform = SearchForm()
    return {
        'forms': form,
        'comment_form': CommentForm(),
        'units': Unit.query.all()
        }

# @main.before_app_request
# def before_request():
#     print([x for x in g])
#     pass

@main.route('/', methods=['GET', 'POST'])
def home():
    # search_google()
    units = Unit.query.all()
    profile_path = url_for('static', filename='unit')
    return render_template('home/home.html')

@main.route('/unit/<int:unit>/lessons')
def lessons_list(unit):
    unit =  Unit.query.get(unit)
    return render_template('lessons/lessons.html', unit=unit)
    
@main.route('/search', methods=['GET', 'POST'])
def search():
    forms = SearchForm()
    if forms.validate_on_submit():
        searc = search_google(forms.search.data)
        # forms = forms.dataload
        
        result = Lesson.query.filter(
            or_(Lesson.content.like(forms.search.data), 
                Lesson.title.like(forms.search.data)              
                                         )).all()
        
        print(Lesson.query.filter(Lesson.content.ilike(forms.search.data)), 'jhay', result, searc)
        return render_template('search/search.html', forms=forms, result=result, search_result=searc)
    return render_template('search/search.html', forms=forms)

@main.route('/unit/<int:unit>/lesson/<int:pk>', methods=['POST', 'GET'])
def lesson(unit, pk):
    """
    A function to handle the display of a specific lesson with associated notes and comments.
    """
    session['last_lesson'] = pk
    print(request.args)
    path = 'audio/unit/%s/lesson/%d/oss.mp3' % (unit, pk)
    session['last_unit'] = unit
    lesson = Lesson.query.get(pk)
    forms = NotesForm()
    comments = Comment.query.all() # where id of comments is equal to the lesson id so that comment for specific lesson will only show
    if forms.validate_on_submit():
        notes = MiniNotes(notes=forms.notes.data)
        notes.save()
        return redirect(url_for('/.lesson', unit=unit, pk=pk))
    print(forms.errors)
    return render_template('lessons/unit1/lesson1.html', lessons=lesson, notes_forms=forms, comments=comments, path=path)

@main.route('/home')
def homepage():
    return redirect('/')


@main.route('/trivia')
def trivia():
    routes = url_for('static', filename='lookinggood.jpg')
    with open('static/trivias.json') as f:
        trivias = json.load(f)
        print(trivias)
    return render_template('trivias/trivia.html', trivias=trivias, image=routes)

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
    """ this shows what happens through out the history"""
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
#         response = convo.last.textry
#         print(response[3:])
#         return render_template('chatbot/chatbot.html', response=response, forms=forms)
#     response = convo.last.text
#     print(forms.errors)
#     return render_template('chatbot/chatbot.html', response=response[4:], forms=forms)



@main.route('/timeline')
def timeline():
    return render_template('timeline/zoom.html')

def get_response_chatbot(txt):
    pass


@main.route('/heroes/')
def heroes():
    """
    List of all the heroes will be displayed here and when the use click
    on certain hero he will be redirected to that hero page

    Hero will either be get through api or database?

    """
    heroes_data  = Hero.query.all()
    return render_template('hero/bookshelf.html', heroes=heroes_data)


@main.route('/hero/<string:first>/<string:last>')
def hero(first, last):
    """
    Single hero page
    """
    name = '{} {}'.format(first, last)
    hero = Hero.query.filter_by(name=name).first()
    print(name, hero)
    print(hero)
    return render_template('hero/hero.html', hero=hero)

# @main.route('unit/<int:unit>/')
@main.route('/audio/unit/<int:unit>/lesson/<int:lesson>')
def play_audio(unit, lesson):
    return render_template('audio.html')
    # path_to_audio = url_for('static', filename='1/1/1.ogg')
    # return send_file(path_to_audio,
    #                  mimetype='audio/wav',
    #                  as_attachment=True, 
    #                  download_name='Unit {} Lesson {}.wav'.format(unit, lesson))
@main.route('/users/bookmark')
def bookmarks():
    bookmarks = BookMark.query.filter_by(user_id=current_user.id).all()
    return render_template('bookmark/bookmark.html', bookmarks=bookmarks)
    
@main.route('/bookmark/lesson/<int:pk>')
def bookmark_function(pk):
    last_lesson = session.get('last_lesson')
    last_unit = session.get('last_unit')

    
    lesson = Lesson.query.get(pk)
    bookmark = BookMark(user_id=1, lesson_id=lesson.id)
    db.session.add(bookmark)
    db.session.commit()
    if last_lesson and last_unit:
        return redirect(url_for('/.lesson', unit=last_unit, pk=last_lesson))
    return redirect(url_for('/.bookmarks'))




@main.route('/presidents')
def presidents():
    president = President.query.order_by(President.name).all()

    return render_template('president/presidents_list.html', presidents=president)
@main.route('/president/<string:name>')
def president(name):
    """
    Single page view of the president of the philippines
    """
    president = President.query.filter_by(name=name)
    return render_template('president/president.html', president='name')


@main.route('/history/quest')
def pquest():
    return render_template('game/quest.html')



