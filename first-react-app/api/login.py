from app import app
from flask import render_template, request, json


@app.route('/login')
def login():
    return render_template('signUp.html')


@app.route('/login_page', methods=['GET', 'POST'])
def screening():
    user = request.form['username']
    password = request.form['password']
    return json.dumps({'status': 'OK', 'user': user, 'pass': password})
