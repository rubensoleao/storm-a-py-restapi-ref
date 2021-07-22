import pytest
from ..mglu.db.client import client
from datetime import datetime

from ..app import app


@pytest.fixture(name="flask_client")
def fixture_flask_client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.fixture(name="client")
def fixture_client():
    return client


@pytest.fixture(name="mock_id")
def fixture_mock_id():
    return "-1"


@pytest.fixture(name="mock_schedule")
def fixture_mock_schedule():
    return {
        "scheduled_date": str(datetime.utcnow()),
        "type": "email",
        "destination": "test@email.com",
        "message": "96c1a5a9-96d8-4dc5-a601-2920f3525cc7",
        "status": "pending",
    }


@pytest.fixture(name="db_init")
def fixture_db_init(mock_schedule, mock_id):
    with client.get_session() as session:
        init_query = "INSERT INTO MSGSCHEDULES (id, scheduled_date, type, destination, message, status) VALUES (:id, :scheduled_date, :type, :destination, :message, :status)"
        session.execute(
            init_query,
            {
                "id": mock_id,
                "scheduled_date": {mock_schedule.get("scheduled_date")},
                "type": {mock_schedule.get("type")},
                "destination": {mock_schedule.get("destination")},
                "message": {mock_schedule.get("message")},
                "status": {mock_schedule.get("status")},
            },
        )
        session.commit()

    yield


@pytest.fixture(name="db_init_multiple")
def fixture_db_init_multiple(mock_schedule, mock_id):
    with client.get_session() as session:
        init_query = "INSERT INTO MSGSCHEDULES (id, scheduled_date, type, destination, message, status) VALUES (:id, :scheduled_date, :type, :destination, :message, :status)"
        session.execute(
            init_query,
            {
                "id": mock_id,
                "scheduled_date": {mock_schedule.get("scheduled_date")},
                "type": {mock_schedule.get("type")},
                "destination": {mock_schedule.get("destination")},
                "message": {mock_schedule.get("message")},
                "status": {mock_schedule.get("status")},
            },
        )

        init_query = "INSERT INTO MSGSCHEDULES (id, scheduled_date, type, destination, message, status) VALUES (:id, :scheduled_date, :type, :destination, :message, :status)"
        session.execute(
            init_query,
            {
                "id": "-11",
                "scheduled_date": {mock_schedule.get("scheduled_date")},
                "type": {mock_schedule.get("type")},
                "destination": {mock_schedule.get("destination")},
                "message": {mock_schedule.get("message")},
                "status": {mock_schedule.get("status")},
            },
        )
        session.commit()

    yield


@pytest.fixture(name="db_teardown")
def fixture_db_teardown(mock_schedule):
    yield

    with client.get_session() as session:
        teardown_query = "DELETE FROM MSGSCHEDULES WHERE MESSAGE=:message"
        session.execute(
            teardown_query,
            {
                "message": {mock_schedule.get("message")},
            },
        )
        session.commit()


@pytest.fixture(name="db_validate_delete")
def fixture_db_validate_delete(mock_id):
    yield

    with client.get_session() as session:
        teardown_query = "SELECT id FROM MSGSCHEDULES WHERE id=:id"
        result = session.execute(
            teardown_query,
            {
                "id": mock_id,
            },
        )

        session.commit()

        assert len(result.all()) == 0
