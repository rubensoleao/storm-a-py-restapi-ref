def test_invalid_id(flask_client):
    """If ID is not num should get validation error"""

    response = flask_client.get(f"/msg-scheduler?id=abcde")
    assert response.status_code == 400
    assert response.json == {"message": "id: Not a valid integer."}


def test_missing_POST_data(flask_client):
    """If call type is not valid should get validation error"""
    response = flask_client.post("/msg-scheduler")

    assert response.status_code == 400


def test_ivalid_call_type(flask_client, mock_schedule):
    """If call type is not valid should get validation error"""
    mock_schedule["type"] = "XXXXXXXXX"
    response = flask_client.post("/msg-scheduler", json=mock_schedule)

    assert response.status_code == 400
    assert "message" in response.json.keys()


def test_email_invalid(flask_client, mock_schedule):
    """If email is not valid should get validation error"""
    mock_schedule["destination"] = "abcdefg"
    response = flask_client.post("/msg-scheduler", json=mock_schedule)

    assert response.status_code == 400
    assert response.json == {"message": "destination: Invalid email adress"}


def test_phone_invalid(flask_client, mock_schedule, db_teardown):
    """If phone is not valid should get validation error"""
    mock_schedule["type"] = "sms"
    mock_schedule["destination"] = "abcdefg"
    response = flask_client.post("/msg-scheduler", json=mock_schedule)

    assert response.status_code == 400
    assert response.json == {"message": "destination: Invalid phone number"}


def test_phone_valid(flask_client, mock_schedule, db_teardown):
    """If phone is valid should not get validation error"""
    mock_schedule["type"] = "whatsapp"
    mock_schedule["destination"] = "1699999999"
    response = flask_client.post("/msg-scheduler", json=mock_schedule)

    assert response.status_code == 201
