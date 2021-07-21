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
