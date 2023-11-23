from flask import Blueprint, jsonify, request
from models.favorite import Favorite
from models.people import People
from models.planet import Planet
from models.user import User

api = Blueprint('api_favorites', __name__)

@api.route('/favorite/planet/<int:id>', methods=['POST'])
def add_favorite_planet(id):
    data = request.get_json()
    user_id = data['user_id']
    test = User.query.get(user_id)
    if not test:
        return jsonify({"message": "User not found"}), 404    
    favorite = Favorite()
    favorite.id_user = user_id
    favorite.id_planet = id
    favorite.save()

    return jsonify({"messsage": "added favorite"}), 200

@api.route('/favorite/people/<int:id>', methods=['POST'])
def add_favorite_people(id):
    data = request.get_json()
    user_id = data['user_id']
    test = User.query.get(user_id)
    if not test:
        return jsonify({"message": "User not found"}), 404    
    favorite = Favorite()
    favorite.id_user = user_id
    favorite.id_people = id
    favorite.save()

    return jsonify({"messsage": "added favorite"}), 200

@api.route('/favorite/people/<int:id>', methods=['DELETE'])
def delete_favorite_people(id):
    favorite = Favorite.query.filter_by(id_people=id)
    if not favorite:
        return jsonify({"message": "favorite not found with specific information"}), 404
    favorite.delete()
    return jsonify({"messsage": "favorite deleted"}), 200

@api.route('/favorite/planet/<int:id>', methods=['DELETE'])
def delete_favorite_planet(id):
    favorite = Favorite.query.filter_by(id_planet=id)
    if not favorite:
        return jsonify({"message": "favorite not found with specific information"}), 404
    favorite.delete()
    test = favorite.serialize()
    return jsonify(test), 200