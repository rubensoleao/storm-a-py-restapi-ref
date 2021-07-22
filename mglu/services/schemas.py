from marshmallow import Schema, post_load, pre_load
from marshmallow.decorators import validates
from marshmallow.exceptions import ValidationError
from marshmallow.fields import DateTime, Integer, String

from ..settings import destination_types


class MsgSchedulesPostRequestSchema(Schema):
    scheduled_date = DateTime(required=True)
    type = String(required=True, max=10)
    destination = String(required=True, max=30)
    message = String(required=True, allow_none=True, max=255)
    status = String(required=False, max=10)

    @pre_load
    def set_status_default(self, data, **kwargs):
        data["status"] = "waiting"
        return data


class MsgSchedulePostResponseSchema(Schema):
    id = Integer()


class MsgSchedulesGetParamsSchema(Schema):
    id = Integer(required=True)


class MsgScheduleGetResponseSchema(Schema):
    id = Integer()
    scheduled_date = DateTime()
    type = String()
    destination = String()
    message = String()
    status = String()

    @pre_load
    def format_date(self, data, many, **kwargs):
        data["scheduled_date"] = str(data["scheduled_date"])

    @post_load
    def format_date(self, item, many, **kwargs):
        item["scheduled_date"] = str(item["scheduled_date"])
        return item


class MsgScheduleDeleteParamsSchema(Schema):
    id = Integer(required=True)


class MsgScheduleDeleteResponseSchema(Schema):
    id = Integer()
