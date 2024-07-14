# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    followers = db.relationship('Follow', backref='followed', lazy='dynamic', foreign_keys='Follow.followed_id')
    following = db.relationship('Follow', backref='follower', lazy='dynamic', foreign_keys='Follow.follower_id')

class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
