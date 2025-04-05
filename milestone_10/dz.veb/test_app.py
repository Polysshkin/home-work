import pytest
from app import app, read_csv, get_birthdays_for_month
from unittest.mock import patch, mock_open
from io import StringIO

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

def test_read_csv_success():
    mock_csv = "Name,Month\nJohn,January\nJane,February\n"
    with patch("builtins.open", return_value=StringIO(mock_csv)):
        result = read_csv('birthdays.csv')
        assert len(result) == 2
        assert result[0]['Name'] == "John"
        assert result[1]['Month'] == "February"

def test_read_csv_failure():
    with patch("builtins.open", mock_open(read_data="")):
        with pytest.raises(ValueError):
            read_csv('birthdays.csv')

def test_read_corrupted_csv():
    corrupted_csv = "Name,Month\nJohn,January\nJane,"
    with patch("builtins.open", return_value=StringIO(corrupted_csv)):
        with pytest.raises(ValueError, match="Row has missing or invalid values"):
            read_csv('birthdays.csv')


def test_get_birthdays_for_month():
    birthdays = [
        {'Name': 'John', 'Month': 'January'},
        {'Name': 'Jane', 'Month': 'February'}
    ]
    january_birthdays = get_birthdays_for_month(birthdays, 'January')
    assert len(january_birthdays) == 1
    assert january_birthdays[0]['Name'] == 'John'

def test_get_birthdays_for_invalid_month():
    birthdays = [
        {'Name': 'John', 'Month': 'January'},
        {'Name': 'Jane', 'Month': 'February'}
    ]
    result = get_birthdays_for_month(birthdays, 'InvalidMonth')
    assert len(result) == 0

def test_birthdays_route(client, mock_csv):
    response = client.get('/birthdays/January')
    assert response.status_code == 200
    assert b'John' in response.data

def test_birthdays_route_invalid_month(client):
    response = client.get('/birthdays/InvalidMonth')
    assert response.status_code == 500

def test_birthdays_route_invalid_month_empty(client):
    response = client.get('/birthdays/')
    assert response.status_code == 404

def test_birthdays_route_invalid_month_special_chars(client):
    response = client.get('/birthdays/!@#')
    assert response.status_code == 500
