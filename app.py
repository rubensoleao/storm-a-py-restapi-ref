import json
from http import HTTPStatus

from flask import Flask
from flask import request as flask_request
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import NoResultFound

from .mglu.db.client import client
from .mglu.services.functions import delete_schedule, get_schedule, post_schedule

app = Flask(__name__)


@app.route("/msg-scheduler", methods=["POST", "GET", "DELETE"])
def hello_world():
    if flask_request.method == "POST":
        request_data = flask_request.get_json()

        processed_response = post_schedule(client, request_data)

        return app.response_class(
            response=json.dumps(processed_response),
            status=HTTPStatus.CREATED,
        )
    elif flask_request.method == "GET":
        request_id = {"id": flask_request.args.get("id")}
        processed_response = get_schedule(client, request_id)
        return app.response_class(
            status=HTTPStatus.OK,
            response=json.dumps(processed_response),
            mimetype="application/json",
        )
    elif flask_request.method == "DELETE":
        request_id = {"id": flask_request.args.get("id")}
        processed_response = delete_schedule(client, request_id)
        return app.response_class(
            status=HTTPStatus.OK,
            response=json.dumps(processed_response),
            mimetype="application/json",
        )
    else:
        return app.response_class(
            status=HTTPStatus.BAD_REQUEST,
            response="Unsupported method",
            mimetype="application/json",
        )


@app.errorhandler(NoResultFound)
def handle_no_result(e):
    return app.response_class(
        status=HTTPStatus.NOT_FOUND,
        response="The requested object was not found",
        mimetype="application/json",
    )


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    message = ""
    for key in e.messages:
        message += f"{key}:"
        for item in e.messages[key]:
            message += f" {item}"
    return app.response_class(
        status=HTTPStatus.BAD_REQUEST,
        response=json.dumps({"message": message}),
        mimetype="application/json",
    )
