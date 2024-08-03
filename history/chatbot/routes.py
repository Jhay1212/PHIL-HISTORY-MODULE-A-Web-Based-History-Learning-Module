from flask import Blueprint, render_template, redirect, url_for, request

cbot = Blueprint('chatbot', __name__, template_folder='templates')

@cbot.route('/chatbot')
def main():
    return render_template('main.html')

@cbot.route('/get', methods=['POST'])
def chatbot_response():
    # msg = 
    pass 