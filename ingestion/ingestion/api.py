from flask import current_app, jsonify
from flask.typing import ResponseReturnValue

from ingestion.db import db


@current_app.route("/ping", methods=["GET"])
def ping() -> ResponseReturnValue:
    return jsonify(message="Ping!"), 200
