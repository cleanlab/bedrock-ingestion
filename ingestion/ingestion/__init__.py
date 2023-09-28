import os

from flask import Flask
from sqlalchemy import text

# initialize flask app and configure database URI
app = Flask(__name__)

env = os.environ
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{env['DB_USERNAME']}:{env['DB_PASSWORD']}@{env['DB_HOST']}:{env['DB_PORT']}/{env['DB_NAME']}"


with app.app_context():
    import ingestion.api
    from ingestion.db import db, initialize_db

    initialize_db(app)

    try:
        # setup dummy data to use when testing `/view` function
        db.session.execute(
            text("CREATE TABLE dummy_data (foo int, bar varchar, baz varchar)"),
        )
        db.session.execute(
            text(
                "INSERT INTO dummy_data (foo, bar, baz) "
                "VALUES "
                "(1, 'bar1', 'blah'), "
                "(2, 'bar2', 'halb')"
            )
        )
        db.session.commit()
    except:
        # dummy data already created
        pass
