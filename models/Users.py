from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    attendance = db.Column(db.Float)
    section = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self,id,name,age,attendance,section,is_active=True):
        self.id = id
        self.name = name
        self.age = age
        self.attendance = attendance
        self.section = section
        self.is_active = is_active
    
    def __repr__(self):

        return f'{self.name} : {self.id}'

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
        

