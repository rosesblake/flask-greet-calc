from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def greet_user():
    """greet user on landing"""
    return 'welcome'

@app.route('/welcome/home')
def greet_user_home():
    """greet user on landing"""
    return 'welcome home'

@app.route('/welcome/back')
def greet_user_back():
    """greet user on landing"""
    return 'welcome back'