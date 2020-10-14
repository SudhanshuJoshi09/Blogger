from app import app
from flask import Flask, render_template, request, json

'''
@app.route('/signUp')
def signUp():
    return render_template('signUp.html')
'''


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        user =  request.form['username'];
        password = request.form['password'];
        return 'hello, world'

    return render_template('signUp.html')

