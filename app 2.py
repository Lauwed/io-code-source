from flask import Flask, url_for, render_template, request


app = Flask(__name__)

@app.route('/')
def index() :
    return 'Index page'

@app.route('/hello')
@app.route('/hello/username')
def hello(username = None) :
    if username :
        return 'Hello %s !' % username
    else :
        return'Hello !'

@app.route('/login', methods=['POST', 'GET'])
def login() :
    if request.method == 'POST' :
        return hello(request.form['username'])
    return render_template('login.html')

with app.test_request_context() :
    url_for('static', filename='style.css')