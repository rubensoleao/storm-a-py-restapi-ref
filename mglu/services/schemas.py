from marshmallow import Schema
from marshmallow.fields import DateTime, Integer, String


class MsgSchedulesPostRequestSchema(Schema):
    scheduled_date = DateTime()
    type = String()
    destination = String()
    message = String()
    status = String()


class MsgSchedulePostResponseSchema(Schema):
    id = Integer()


class MsgSchedulesGetParamsSchema(Schema):
    id = Integer()


class MsgScheduleGetResponseSchema(Schema):
    id = Integer()
    scheduled_date = DateTime()
    type = String()
    destination = String()
    message = String()
    status = String()


class MsgScheduleDeleteParamsSchema(Schema):
    id = Integer()


class MsgScheduleDeleteResponseSchema(Schema):
    id = Integer()
