# pylint: disable=unused-argument
import json


def test_get_schedule(flask_client, mock_id, db_init, db_teardown):
    """Test getting a schedule."""

    response = flask_client.get(f"/msg-scheduler?id={mock_id}")
    assert response.status_code == 200


def test_post_schedule(flask_client, mock_id, mock_schedule, db_teardown):
    """Test getting a schedule."""

    response = flask_client.post("/msg-scheduler", json=mock_schedule)
    assert response.status_code == 201


def test_delete_schedule(flask_client, mock_id, db_init, db_teardown):
    """Test getting a schedule."""

    response = flask_client.delete(f"/msg-scheduler?id={mock_id}")
    assert response.status_code == 200


def test_id_not_found_get(flask_client):
    """Tests GET with an ID not found"""

    response = flask_client.get(f"/msg-scheduler?id=-10")
    assert response.status_code == 404


def test_id_not_found_delete(flask_client):
    """Tests DELETE with an ID not found"""

    response = flask_client.delete(f"/msg-scheduler?id=-10")

    assert response.status_code == 200
