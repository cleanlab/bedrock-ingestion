import os

from flask import Flask, jsonify
from flask.typing import ResponseReturnValue

# initialize flask app and configure database URI
app = Flask(__name__)

env = os.environ
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{env['DB_USERNAME']}:{env['DB_PASSWORD']}@{env['DB_HOST']}:{env['DB_PORT']}/{env['DB_NAME']}"


with app.app_context():
    import ingestion.api
    from ingestion.db import initialize_db

    initialize_db(app)
