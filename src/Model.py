# src/models.py
import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_postgres_db(app):
    """
    setup POSTGRES db
    """
    POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432'}

    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
    %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    db.app = app
    db.init_app(app)

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
        self.level_0 = level_0
        self.index = index
        self.overall= overall
        self.verified= verified
        self.reviewTime= reviewTime
        self.reviewerID= reviewerID
        self.productID= productID
        self.reviewerName= reviewerName
        self.reviewText=reviewText
        self.summary=summary
        self.unixReviewText= unixReviewText
        self.vote=vote
        

    def __repr__(self):
        return '<User {}>'.format(self.level_0)