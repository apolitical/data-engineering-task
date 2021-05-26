# app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'reviews'
    level_0 = db.Column(db.Integer, primary_key=False)
    index = db.Column(db.Integer, index=True, unique=True)
    overall = db.Column(db.Float, index=True, unique=True)
    verified = db.Column(db.Integer, primary_key=True)
    reviewTime = db.Column(db.String(120), index=True, unique=True)
    reviewerID = db.Column(db.String(120), index=True, unique=True)
    productID = db.Column(db.String(120), primary_key=True)
    reviewerName = db.Column(db.String(120), index=True, unique=True)
    reviewText = db.Column(db.String(120), index=True, unique=True)
    summary = db.Column(db.String(120), primary_key=True)
    unixReviewText = db.Column(db.Integer, index=True, unique=True)
    vote = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, level_0, index, overall, verified, reviewTime, reviewerID,productID, reviewerName,reviewText, summary,unixReviewText, vote):
        self.title = title
        self.release_date = release_date
        


    def __repr__(self):
        return '<User {}>'.format(self.id)