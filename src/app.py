# app.py
# provides the Flask application
import os
from flask import Flask, Response
from sqlalchemy import create_engine
from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy
#from model import setup_postgres_db

# create a Flask app
app = Flask(__name__) 

#setting up postgres
#setup_postgres_db(app)

# for queries
db_engine = create_engine("sqlite:///data/musical_instrument_reviews.sqlite")


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

