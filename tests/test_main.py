# skripta za testiranje naše aplikacije

import os
import pytest

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from main import app, db

@pytest.fixture
def client():
    client = app.test_client()

    cleanup()

    db.create_all()

    yield client

def cleanup():
    db.drop_all()

def test_index_not_logged(client):
    response = client.get("/")
    assert b"Enter your name" in response.data

def test_index_logged(client):
    client.post("/login", data={"user-name": "Test User", "user-email": "test@user.com", "user-password": "pass123"}, follow_redirects=True)

    response = client.get("/")
    assert b"Enter your guess" in response.data