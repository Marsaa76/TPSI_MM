from flask import Flask, request, jsonify
from models import db, City
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/cities', methods=['GET'])
def get_all_cities():
    cities = City.query.all()
    return jsonify([city.to_dict() for city in cities])