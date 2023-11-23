from flask import Blueprint, jsonify, request
from models.user import User

api = Blueprint('api_users', __name__)

@api.route('/users', methods=['GET'])
def list_users():

    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200

@api.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new = User()
    new.username = data['username']
    new.save()

    return jsonify({ "message": "User added"}), 200

@api.route('/users', methods=['PUT'])
def update_user():
    data = request.get_json()
    id = data['id']
    new = User.query.get(id)
    if not new:
        return jsonify({"message": "User not found"}), 404
    new.username = data['username']
    new.save()

    return jsonify({ "message": "User updated"}), 200

@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    user.delete()

    return jsonify({ "message": "User deleted"}), 200

@api.route('/users/favorites/<int:id>', methods=['GET'])
def list_favorites(id):
    current = User.query.get(id)
    if not current:
        return jsonify({"message": "User not found"}), 404
    
    favorites = current.list_favorites()
    return jsonify(favorites)