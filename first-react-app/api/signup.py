from app import app
from flask import render_template, request

'''
@app.route('/signUp')
def signUp():
    return render_template('signUp.html')
'''


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        return f'{user} and {password}'

    return render_template('signUp.html')
