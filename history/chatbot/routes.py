from flask import Blueprint, render_template, redirect, url_for, request, current_app
from flask import Flask, request, jsonify

from .forms import Chatbot
from .utils import predict_class, get_response


# from . import train
cbot = Blueprint('chatbot', __name__, template_folder='templates')

@cbot.route('/chatbot')
def main():
    return render_template('main.html')

@cbot.route('/get', methods=['POST'])
def chatbot_response():
    # msg = 
    pass 


@cbot.route('/jhay')
def chat_now():
    return render_template('xxx.html')
@cbot.route('/handle/message', methods=['GET', 'POST'])
def handle_message():
    message = request.json['message']
    intent_list = predict_class(message)
    response = get_response(intent_list)

    return jsonify({'response': response})

@cbot.route('/chat0', methods=['POST', 'GET'])
def chat():
    pass

print(cbot.static_url_path)