def test_get_schedule(client, mock_id, db_init, db_teardown):
    """Test getting a schedule."""
    params = {"id": mock_id}
    response = get_schedule(client, params)
    assert str(response["id"]) == mock_id


def test_get_schedule(flask_client, mock_id, db_init, db_teardown):
    """Test getting a schedule."""

    response = flask_client.get(f"/msg-scheduler?id={mock_id}")
    assert response.status_code == 200
