#creates flask app for use


from flask import Flask

#ORM of database
from flask_sqlalchemy import SQLAlchemy

#used for migration of data
from flask_migrate import Migrate

#instant of database
db=SQLAlchemy()

#method returns flask application
def create_app():
        
        #creating flask app
        flask_app=Flask(__name__)
        flask_app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./users.db'
        #defining the path of our database
        migrate= Migrate(flask_app, db)
        db.init_app(flask_app)

       



        return flask_app