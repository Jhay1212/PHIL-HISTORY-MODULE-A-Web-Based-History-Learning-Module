from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for

from history.auth.models import User

socmed = Blueprint('social', __name__, template_folder='templates')

@socmed.route('/history/media', methods=['GET', 'POST'])
def socmed_home():
    return render_template('socmed/home.html')

@socmed.route('/history/profile/user/<string:username>')
def socmed_profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template('socmed/profile.html', profile=user)


