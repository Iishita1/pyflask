from app import db



class Person(db.Model):
    __tablename__= 'usertable'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    job=db.Column(db.Text)
    dob=db.Column(db.Date)
