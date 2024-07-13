from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, request, session

from flask_login import current_user, login_required

from history import db
from history.auth.models import User

from .models import PostComment, PostModel
from .forms import PostForm, EditUserForm

from random import shuffle
from .utils import send_message


socmed = Blueprint('social', __name__, template_folder='templates')

# @socmed.after_request
# def save_response(r):
#     if request.method == 'POST':
#         return r
#     if request.endpoint == 'static':
#         return r
    
#     history = session.get('history', [])
#     if history:
#         if history[-1][0] == request.endpoint and history[-1][1] == request.view_args:
#             return r

#     history.append(
#         request.endpoint,
#         request.view_args,
#         r.response_code
#     )
#     session['history'] = history[-5:]
#     return r 

@socmed.route('/media/feed', methods=['GET', 'POST'])
def feed():
    forms = PostForm()
    if forms.validate_on_submit():
        post = PostModel(user_id=1, title=forms.title.data, category=forms.category.data)
        comment = PostComment(post_id=post.id, comment=send_message(post.title), post=post)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('social.feed'))
    posts = PostModel.query.all()
    if request.method == 'POST':
        pass

    print([x for x in posts])
    return render_template('socmed/home.html', posts=posts, forms=forms)

@socmed.route('/profile/user/<string:username>')
def socmed_profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template('socmed/profile.html', profile=user)


@socmed.route('/profile/edit/user', methods=['GET', 'POST'])
@login_required
def edit_user():
    forms = EditUserForm()
    if forms.validate_on_submit():
        current_user.username = forms.username.data
        current_user.email = forms.email.data
        current_user.password = forms.password.data
        db.session.commit()
        return redirect(url_for(''))
    if request.methods == 'GET':
        forms.username.data = current_user.username
        forms.email.data = current_user.email
        return render_template('edit_user.html', forms=forms, user=current_user)


# @socmed.route('/add/post', methods=['GET', 'POST'])
# def add_post():

#     forms = PostForm()
#     if forms.validate_on_submit():
#         post = forms.