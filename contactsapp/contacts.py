from flask import blueprints, jsonify, request
from contactsapp.db_con import db
from contactsapp.models import Contact


contacts_bp = blueprints.Blueprint("contacts", __name__, url_prefix="/api/v1/contacts")


@contacts_bp.route("/", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    if not contacts:
        return jsonify({'message': 'No contacts found'}), 404
    return jsonify({'contacts': [contact.serializer() for contact in contacts]}), 200


@contacts_bp.route("/<int:contact_id>", methods=["GET"])
def get_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404
    return jsonify({'contact': contact.serializer()}), 200


@contacts_bp.route("/", methods=["POST"])
def add_contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    if not name or not email or not phone:
        return jsonify({'message': 'Name, email, and phone are required'}), 400

    if Contact.query.filter((Contact.email == email) | (Contact.phone == phone)).first():
        return jsonify({'message': 'Contact with this email or phone already exists'}), 409

    new_contact = Contact(name=name, email=email, phone=phone)
    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Contact added successfully', 'contact': new_contact.serializer()}), 201


@contacts_bp.route("/<int:contact_id>", methods=["PUT"])
def update_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404

    data = request.get_json()
    contact.name = data.get("name", contact.name)
    contact.email = data.get("email", contact.email)
    contact.phone = data.get("phone", contact.phone)

    db.session.commit()

    return jsonify({'message': 'Contact updated successfully', 'contact': contact.serializer()}), 200


@contacts_bp.route("/<int:contact_id>", methods=["PATCH"])
def partial_update_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404

    data = request.get_json()
    if "name" in data:
        contact.name = data["name"]
    if "email" in data:
        contact.email = data["email"]
    if "phone" in data:
        contact.phone = data["phone"]

    db.session.commit()

    return jsonify({'message': 'Contact partially updated successfully', 'contact': contact.serializer()}), 200


@contacts_bp.route("/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)
    if not contact:
        return jsonify({'message': 'Contact not found'}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({'message': 'Contact deleted successfully'}), 200