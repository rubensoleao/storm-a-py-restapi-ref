# pylint: disable=unused-argument
from sqlalchemy.sql.elements import ReleaseSavepointClause
from ..mglu.services.clients import post_schedule, get_schedule, delete_schedule


def test_post_schedule(client, mock_schedule, db_teardown):
    """Test posting a schedule."""
    response = post_schedule(client, mock_schedule)

    assert "id" in response.keys()


def test_get_schedule(client, mock_id, db_init, db_teardown):
    """Test getting a schedule."""
    params = {"id": mock_id}
    response = get_schedule(client, params)
    assert str(response["id"]) == mock_id


def test_delete_schedule(client, mock_id, db_init, db_validate_delete):
    """Test deleting a schedule."""
    params = {"id": mock_id}
    response = delete_schedule(client, params)
    assert str(response["id"]) == mock_id
