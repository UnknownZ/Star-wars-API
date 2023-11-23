from flask import Blueprint, jsonify, request
from models.planet import Planet

api = Blueprint('api_planets', __name__)

@api.route('/planets', methods=['GET'])
def list_planets():

    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.serialize(), planets))

    return jsonify(planets), 200

@api.route('/planets/<int:id>', methods=['GET'])
def list_users_liked(id):
    planet = Planet.query.get(id)
    if not planet:
        return jsonify({"message": "Planet not found"}), 404

    return jsonify(planet), 200

@api.route('/planets', methods=['POST'])
def add_planet():
    data = request.get_json()
    new = Planet()
    new.name = data['name']
    new.save()

    return jsonify({ "message": "Planet added"}), 200

@api.route('/planets', methods=['PUT'])
def update_planet():
    data = request.get_json()
    id = data['id']
    new = Planet.query.get(id)
    if not new:
        return jsonify({"message": "Planet not found"}), 404
    new.name = data['name']
    new.save()

    return jsonify({ "message": "Planet updated"}), 200

@api.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)
    if not planet:
        return jsonify({"message": "Planet not found"}), 404
    planet.delete()

    return jsonify({ "message": "Planet deleted"}), 200