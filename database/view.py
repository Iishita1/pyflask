from flask import render_template,redirect,url_for

from models import Person
def routes(app, db):

    #route to home page
    @app.route('/')
    def home():
        return render_template('index.html')
    