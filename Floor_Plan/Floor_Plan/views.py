"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Floor_Plan import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index1.html',
        title='1st Floor',
        year=datetime.now().year,
    )

@app.route('/index2.cshtml')
def index2():
    return render_template(
        'index2.html',
        title='2nd Floor',
        year=datetime.now().year,
    )

@app.route('/index3.cshtml')
def index3():
    return render_template(
        'index3.html',
        title='3rd Floor',
        year=datetime.now().year,
    )
