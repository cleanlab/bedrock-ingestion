from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initialize_db(app) -> None:
    db.app = app
    db.init_app(app)
