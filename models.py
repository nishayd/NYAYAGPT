from database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    is_admin =db.Column(db.Boolean,default=False)

class QuestionHistory(db.Model):
    __tablename__ = 'questionhistory'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question = db.Column(db.Text)
    sector = db.Column(db.String(100))
    response = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class UnansweredQuestion(db.Model):
    __tablename__ = 'unansweredquestion'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    sector = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class ContactQuery(db.Model):
    __tablename__ = 'contact_query'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    subject = db.Column(db.String(200))
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
