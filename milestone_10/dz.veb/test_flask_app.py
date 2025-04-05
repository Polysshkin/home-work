import pytest
from flask.testing import FlaskClient
from app import app
from unittest.mock import patch, mock_open

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_csv():
    mock_data = "Name,Month\nJohn,January\nJane,February\n"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        yield

def test_birthdays_route_with_mock(client, mock_csv):
    response = client.get('/birthdays/January')
    assert response.status_code == 200
    assert b'John' in response.data
    assert b'January' in response.data

def test_birthdays_route_invalid_month(client, mock_csv):
    response = client.get('/birthdays/InvalidMonth')
    assert response.status_code == 200
    assert response.data == b'[]\n'
