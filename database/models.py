from app import db



class Person(db.model):
    __tablename__= 'usertable'
    id = db.Coloumn(db.Integer, primary_key=True)
    name=db.coloumn(db.Text)
    age=db.Coloumn(db.integer)
    job=db.Coloumn(db.Text)
