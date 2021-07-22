# pylint: disable=unused-argument
import json


def test_get_schedule_id(flask_client, mock_id, db_init, db_teardown):
    """Test getting a schedule using id."""

    response = flask_client.get(f"/msg-scheduler?id={mock_id}")
    assert response.status_code == 200


def test_get_schedule_message(flask_client, mock_destination, db_init, db_teardown):
    """Test getting a schedule using destination."""
    response = flask_client.get(f"/msg-scheduler?destination={mock_destination}")
    assert response.status_code == 200


def test_post_schedule(flask_client, mock_id, mock_schedule, db_teardown):
    """Test getting a schedule."""

    response = flask_client.post("/msg-scheduler", json=mock_schedule)
    assert response.status_code == 201


def test_delete_schedule(flask_client, mock_id, db_init, db_teardown):
    """Test getting a schedule."""

    response = flask_client.delete(f"/msg-scheduler?id={mock_id}")
    assert response.status_code == 200


def test_pagination(
    flask_client, mock_id, mock_schedule, db_init_multiple, db_teardown
):
    """Test pagination for schedule."""
    response = flask_client.get(f"/msg-scheduler?page=1&limit=1")

    assert response.status_code == 200
    assert response.json["page"] == 1
    assert response.json["total"] == 2
    response = flask_client.get(f"/msg-scheduler?page=2&limit=1")
    assert response.status_code == 200
    assert response.json["page"] == 2
    assert response.json["total"] == 2
    response = flask_client.get(f"/msg-scheduler?page=3&limit=1")
    assert response.status_code == 404


def test_id_not_found_get(flask_client):
    """Tests GET with an ID not found"""

    response = flask_client.get(f"/msg-scheduler?id=-10")

    assert response.status_code == 404


def test_id_not_found_delete(flask_client):
    """Tests DELETE with an ID not found"""

    response = flask_client.delete(f"/msg-scheduler?id=-10")

    assert response.status_code == 200
