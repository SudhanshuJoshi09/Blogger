from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from routes import *
from signup import *
from login import *

if __name__ == '__main__':
    app.run(debug=True)
