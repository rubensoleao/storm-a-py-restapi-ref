# pylint: disable=unused-argument
from ..mglu.services.clients import   post_schedule

def test_post_schedule(client, mock_schedule):
    """Test posting a schedule."""
    post_schedule(client, mock_schedule)