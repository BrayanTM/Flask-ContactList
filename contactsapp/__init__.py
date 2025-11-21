from flask import Flask
from flask_migrate import Migrate
from contactsapp.db_con import db
from contactsapp import contacts
from contactsapp import models  # noqa: F401 - Necesario para Flask-Migrate


migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(contacts.contacts_bp)

    return app