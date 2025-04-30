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

@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    city = City.query.get(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    
    data = request.get_json()
    
    try:
        if 'name' in data:
            city.name = data['name']
        if 'country' in data:
            city.country = data['country']
        if 'population' in data:
            city.population = int(data['population'])
        if 'area' in data:
            city.area = float(data['area'])
        if 'last_population_update' in data:
            city.last_population_update = datetime.strptime(data['last_population_update'], '%Y-%m-%d').date()
        
        db.session.commit()
        return jsonify(city.to_dict())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.query.get(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    
    db.session.delete(city)
    db.session.commit()
    return jsonify({'message': 'City deleted successfully'}), 200
@app.route('/cities/statistics/population', methods=['GET'])
def get_cities_by_population():
    min_population = request.args.get('minPopulation', type=int)
    max_population = request.args.get('maxPopulation', type=int)
    
    if min_population is None or max_population is None:
        return jsonify({'error': 'Both minPopulation and maxPopulation parameters are required'}), 400
    
    if min_population > max_population:
        return jsonify({'error': 'minPopulation must be less than or equal to maxPopulation'}), 400
    
    cities = City.query.filter(
        City.population >= min_population,
        City.population <= max_population
    ).all()
    
    return jsonify([city.to_dict() for city in cities])
@app.route('/cities/statistics/area', methods=['GET'])
def get_cities_by_area():
    min_area = request.args.get('minArea', type=float)
    max_area = request.args.get('maxArea', type=float)
    
    if min_area is None or max_area is None:
        return jsonify({'error': 'Both minArea and maxArea parameters are required'}), 400
    
    if min_area > max_area:
        return jsonify({'error': 'minArea must be less than or equal to maxArea'}), 400
    
    cities = City.query.filter(
        City.area >= min_area,
        City.area <= max_area
    ).all()
    
    return jsonify([city.to_dict() for city in cities])
if __name__ == '__main__':
    app.run(debug=True)