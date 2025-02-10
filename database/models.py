from app import db

class Person(db.Model):
    __tabelname__ = 'people'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f'person with name {self.name} and age {self.age}'