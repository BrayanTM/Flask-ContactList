from flask import blueprints, jsonify, request
from contactsapp.db_con import db
from contactsapp.models import Contact


contacts_bp = blueprints.Blueprint("contacts", __name__, url_prefix="/api/v1/contacts")


@contacts_bp.route("/", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.serializer() for contact in contacts]), 200