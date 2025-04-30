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
@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = City.query.get(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.to_dict())
@app.route('/cities', methods=['POST'])
def add_city():
    data = request.get_json()
    
    required_fields = ['name', 'country', 'population', 'area', 'last_population_update']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        last_update = datetime.strptime(data['last_population_update'], '%Y-%m-%d').date()
        new_city = City(
            name=data['name'],
            country=data['country'],
            population=int(data['population']),
            area=float(data['area']),
            last_population_update=last_update
        )
        db.session.add(new_city)
        db.session.commit()
        return jsonify(new_city.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400