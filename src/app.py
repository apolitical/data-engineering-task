# app.py
# provides the Flask application
import os
from flask import Flask, Response
from sqlalchemy import create_engine
from sqlalchemy import inspect
from Model import db

app = Flask(__name__)  # create a Flask app
db_engine = create_engine("sqlite:///data/musical_instrument_reviews.sqlite")


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
    db.init_app(app)


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
    SAMPLE userID=ABLTNLVKCVQMK

    """
    query= 'SELECT * FROM reviews where reviewerID=:user_id;'
    result=db_engine.execute(query, user_id).fetchall()
    return Response(str(result), 200)

