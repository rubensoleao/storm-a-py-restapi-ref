from sqlalchemy import schema
from .schemas import MsgSchedulesPostRequestSchema, MsgSchedulePostResponseSchema


def post_schedule(client, request_data):
    request_schema = MsgSchedulesPostRequestSchema()
    response_schema = MsgSchedulePostResponseSchema()

    validated_request = request_schema.load(request_data)
    db_response = client.post(validated_request)
    response = response_schema.load(db_response)

    return response
