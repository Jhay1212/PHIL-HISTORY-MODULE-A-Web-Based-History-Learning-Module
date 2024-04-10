from flask.blueprints import Blueprint
from flask import render_template, redirect

main = Blueprint('/', __name__, template_folder='templates')

@main.route('/home')
def home():
    return render_template('kasaysayan1.html')

@main.route('/')
def homepage():
    return redirect('home')