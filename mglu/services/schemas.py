from re import S
from marshmallow import Schema, post_load, pre_load
from marshmallow.decorators import validates
from marshmallow.exceptions import ValidationError
from marshmallow.fields import DateTime, Integer, String, Nested, List
from sqlalchemy.sql.roles import LimitOffsetRole

from ..exceptions import MissingPostData, EmptyResult
from ..settings import destination_types
from .utils import validate_email, validate_phone


class MsgSchedulesSchema(Schema):
    id = Integer()
    scheduled_date = DateTime()
    type = String(max=10)
    destination = String(max=30)
    message = String(max=255)
    status = String(max=10)

    @post_load
    def format_date(self, item, many, **kwargs):
        if item.get("scheduled_date"):
            item["scheduled_date"] = str(item["scheduled_date"])
        return item


class MsgSchedulesPostRequestSchema(Schema):
    scheduled_date = DateTime(required=True)
    type = String(required=True, max=10)
    destination = String(required=True, max=30)
    message = String(required=True, allow_none=True, max=255)
    status = String(required=False, max=10)

    @pre_load
    def set_status_default(self, data, **kwargs):
        if not data:
            raise MissingPostData
        data["status"] = "waiting"
        return data

    @validates("type")
    def validate_type(self, value):
        if value not in destination_types:
            raise ValidationError(
                f"Invalid message type must be in {destination_types!r}"
            )

    @post_load
    def validate_destination(self, data, **kwargs):
        if data["type"] == "email":
            if not validate_email(data["destination"]):
                raise ValidationError(
                    field_name="destination", message=f"Invalid email adress"
                )
        elif data["type"] in ("sms", "whatsapp"):
            if not validate_phone(data["destination"]):
                raise ValidationError(
                    field_name="destination", message=f"Invalid phone number"
                )

        return data


class MsgSchedulePostResponseSchema(Schema):
    id = Integer()


class MsgSchedulesGetParamsSchema(MsgSchedulesSchema):
    page = Integer(default=1)
    limit = Integer(default=1)

    @validates("page")
    def validate_page(self, value):
        if value <= 0:
            raise ValueError("page must be greater than 0")

    @validates("limit")
    def validate_limit(self, value):
        if value <= 0:
            raise ValueError("limit must be greater than 0")


class MsgScheduleGetResponseSchema(Schema):
    data = List(Nested(MsgSchedulesSchema))
    page = Integer()
    total = Integer()

    @post_load
    def format_data(self, data, **kwargs):
        print(data)
        if len(data["data"]) == 0:
            raise EmptyResult
        return data


class MsgScheduleDeleteParamsSchema(Schema):
    id = Integer(required=True)


class MsgScheduleDeleteResponseSchema(Schema):
    id = Integer()
