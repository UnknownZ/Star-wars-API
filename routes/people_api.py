from flask import Blueprint, jsonify, request
from models.people import People

api = Blueprint('api_people', __name__)

@api.route('/people', methods=['GET'])
def list_people():

    people = People.query.all()
    people = list(map(lambda people: people.serialize(), people))

    return jsonify(people), 200

@api.route('/people/<int:id>', methods=['GET'])
def list_users_liked(id):
    people = People.query.get(id)
    if not people:
        return jsonify({"message": "People not found"}), 404
    return jsonify(people), 200

@api.route('/people', methods=['POST'])
def add_people():
    data = request.get_json()
    new = People()
    new.name = data['name']
    new.save()

    return jsonify({ "message": "People added"}), 200

@api.route('/people', methods=['PUT'])
def update_people():
    data = request.get_json()
    id = data['id']
    new = People.query.get(id)
    if not new:
        return jsonify({"message": "People not found"}), 404
    new.name = data['name']
    new.save()

    return jsonify({ "message": "People updated"}), 200

@api.route('/people/<int:id>', methods=['DELETE'])
def delete_people(id):
    people = People.query.get(id)
    if not people:
        return jsonify({"message": "People not found"}), 404
    
    people.delete()
    return jsonify({ "message": "People deleted"}), 200


