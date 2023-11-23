import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import db

from models.favorite import Favorite
from models.people import People
from models.planet import Planet
from models.user import User

from rutas import api

from routes.favorites_api import api as api_favorites
from routes.people_api import api as api_people
from routes.planets_api import api as api_planets
from routes.users_api import api as api_users

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)
Migrate(app, db)
CORS(app)

app.register_blueprint(api_users, url_prefix="/api")
app.register_blueprint(api_favorites, url_prefix="/api")
app.register_blueprint(api_planets, url_prefix="/api")
app.register_blueprint(api_people, url_prefix="/api")

@app.route('/')
def main():
    return jsonify({"message": "API REST With Flask"}), 200

if __name__ == '__main__':
    app.run()