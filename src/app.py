# app.py
# provides the Flask application
import os
from flask import Flask, Response
from sqlalchemy import create_engine
from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# for queries
db_engine = create_engine("sqlite:///data/musical_instrument_reviews.sqlite")

# Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/reviews'
db= SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'reviews'
    level_0 = db.Column(db.Integer, primary_key=True)
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


@app.route("/", methods=["GET"])
def root() -> Response:
    """
    root - returns 200 OK
    """
    return Response("It's alive!", status=200)

@app.route("/dbcheck")
def db_check() -> Response:
    """
    table - returns table information
    """
    query ='SELECT * FROM reviews limit 3;'
    result=db_engine.execute(query).fetchall()
    return Response(str(result), 200)


@app.route("/product/<product_id>")
def product_review(product_id: str) -> Response:
    """
    product review - return retrieve aggregated information for a Product
    with a particular ID.
    SAMPLE PRODUCT_ID=0739079891

    """
    query ='SELECT * FROM reviews where productID=:product_id;'
    result=db_engine.execute(query,product_id).fetchall()
    return Response(str(result), 200)



@app.route("/user/<user_id>")
def user_review(user_id: str) -> Response:
    """
    user review - return retrieve aggregated information for a User
    with a particular ID.
    SAMPLE userID=ABLTNLVKCVQMK, -> THIS userIdD belong to 'Mark'

    """
    query= 'SELECT * FROM reviews where reviewerID=:user_id;'
    result=db_engine.execute(query, user_id).fetchall()
    return Response(str(result), 200)

