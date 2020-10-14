from app import app
from flask import Flask, render_template, request, json
from models import db, Users

@app.route('/login')
def login():
    return render_template('signUp.html')


@app.route('/', methods=['GET', 'POST'])
def screening():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});
