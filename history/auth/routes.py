from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, flash
from flask_sqlalchemy import session
from flask_login import login_user, current_user
from flask_mail import Message
from threading import Thread

from history import bcrpyt, login_manager, db, mail_manager, url_back
from history.auth.forms import RegisterForm, LoginForm, RequestResetForm, ResetPasswordForm
from history.auth.models import User

acc = Blueprint('/auth', __name__, template_folder='templates')

# def send_email(user):
#      with acc.app

def send_email(app, msg):
     with app.app_context():
          mail_manager.send(msg)

@acc.route('/signup', methods=['POST', 'GET'])
def register():
    forms = RegisterForm()
    if forms.validate_on_submit():
        message = Message(subject="Account Created", recipients=[forms.email.data], sender='rjhay1070@gmail.com')
        message.body = f'Account Created for {forms.username.data}'

        thread = Thread(target=send_email, args=[forms])
        thread.start()
        # mail_manager.send(message=message)
        password = bcrpyt.generate_password_hash(forms.password.data)
        user = User(username=forms.username.data, email=forms.email.data, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_back())
    else:
        return render_template('signup.html', forms=forms, errors=forms.errors)
         
    print(forms.errors)
    flash(message=forms.errors)
    return render_template('signup.html', forms=forms)


@acc.route('/login', methods=['POST', 'GET'])
def login():

    forms = LoginForm()
    if forms.validate_on_submit():
        user = User.query.filter_by(username=forms.username.data).first()
        if user and bcrpyt.check_password_hash(user.password, forms.password.data):
                login_user(user, remember=True)
                print('1')
                return redirect('/')
        else:
             flash(f'Login Unsuccsesful. PLease Check username or password')
    return render_template('Login1.html', forms=forms)


@acc.route('/request/reset/', methods=['POST', 'GET'])
def request_reset():
     forms = RequestResetForm()
     if forms.validate_on_submit():
          user = User.query.filter_by(email=forms.email.data).first()
          send_email(user)
          return redirect(url_for('login'))
     return render_template('request_reset.html', forms=forms)

    
@acc.route('/reset/<token>')
def reset_password(token):
    forms = ResetPasswordForm()
    user = User.verify_reset_token(token)
    if user is None:
          return redirect(url_for('request_reset'))
    if forms.password.validate():
          new_password = bcrpyt.generate_password_hash(forms.password.data)
          user.password = new_password
          db.commit()
          return redirect(url_for('login'))
    return render_template('reset_password.html', forms=forms)


@acc.route('/logout')
def logout():
    return render_template('logout.html')