# tests/test_app.py
# tests for src/app.py

import pytest
from sqlalchemy import create_engine
from src.app import root,db_check, product_review, user_review

db_engine = create_engine("sqlite:///data/musical_instrument_reviews.sqlite")

def test_root():
    rsp = root()
    assert rsp.data.decode("utf8") == "It's alive!", "Unexpected response message"
    assert rsp.status_code == 200, "Status code was not 200"

def test_db_check():
    db = db_check()
    # Test to make sure that there are 2 items in the database
    assert len(list(db_engine.execute('SELECT * FROM reviews LIMIT 3'))) == 3
    assert db.status_code == 200, "Status code was not 200"

def test_product_review():
    prd=product_review()
    # Test to make sure that there are 2 items in the database
    assert len(list(db_engine.execute('SELECT * FROM reviews LIMIT 3'))) == 3
    assert prd.status_code == 200, "Status code was not 200"

def test_user_review():
    usr=user_review()
    # Test to make sure that there are 2 items in the database
    assert len(list(db_engine.execute('SELECT * FROM reviews LIMIT 3'))) == 3
    assert usr.status_code == 200, "Status code was not 200"



