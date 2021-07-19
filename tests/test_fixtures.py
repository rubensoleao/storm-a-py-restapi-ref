# pylint: disable=unused-argument


def test_dummy():
    assert True


def test_db_fixture(db_init, db_validate_delete, db_teardown):
    assert True
