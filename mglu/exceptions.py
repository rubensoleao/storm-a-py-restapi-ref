from marshmallow.exceptions import ValidationError


class MissingPostData(Exception):
    """Raised when a required post data is missing."""

    message = "Missing required post data"

    def __init__(self):
        super().__init__(self.message)
