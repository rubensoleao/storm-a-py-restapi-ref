from sqlalchemy import schema
from . import schemas


def post_schedule(client, request_data):
    request_schema = schemas.MsgSchedulesPostRequestSchema()
    response_schema = schemas.MsgSchedulePostResponseSchema()

    validated_request = request_schema.load(request_data)
    db_response = client.post(validated_request)
    response = response_schema.load(db_response)

    return response


def get_schedule(client, params):
    params_schema = schemas.MsgSchedulesGetParamsSchema()
    response_schema = schemas.MsgScheduleGetResponseSchema()

    validated_params = params_schema.load(params)
    db_response = client.get(**validated_params)

    response = response_schema.load(db_response)

    return response


def delete_schedule(client, params):
    params_schema = schemas.MsgScheduleDeleteParamsSchema()
    response_schema = schemas.MsgScheduleDeleteResponseSchema()

    validated_params = params_schema.load(params)
    db_response = client.delete(**validated_params)

    response = response_schema.load(db_response)

    return response
