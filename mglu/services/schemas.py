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
