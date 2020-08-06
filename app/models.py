from datetime import datetime

from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from flask_login import UserMixin
from app import login

# Any Flask models ie database tables must inherit from ... db.models
class Person(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Posts', backref='People', lazy=True)
    about_me = db.Column(db.String(340))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())

    def create_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        print(self.password_hash)
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)

# known as one to many
class Posts(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(120), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    # request = db.relationship("Person", backref=backref("People", uselist=False))

    def __repr__(self):
        return '<Posts {}>'.format(self.body)

@login.user_loader
def load_user(id):
    # id is a string so need to convert it to an int
    return Person.query.get(int(id))