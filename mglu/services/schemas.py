from marshmallow import Schema, post_load, pre_load
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
    scheduled_date = DateTime(required=True)
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
    id = Integer()


class MsgScheduleDeleteResponseSchema(Schema):
    id = Integer()
