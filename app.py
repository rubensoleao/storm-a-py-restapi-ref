import json
from http import HTTPStatus

from flask import Flask
from flask import request as flask_request

from .mglu.services.clients import get_schedule, post_schedule
from .mglu.db.client import client

app = Flask(__name__)


@app.route("/msg-scheduler", methods=["POST", "GET"])
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
    else:
        return app.response_class(
            status=HTTPStatus.BAD_REQUEST,
            response="Unsupported method",
            mimetype="application/json",
        )
