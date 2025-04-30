from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    area = db.Column(db.Float, nullable=False)
    last_population_update = db.Column(db.Date, nullable=False)
    def __init__(self, name, country, population, area, last_population_update):
        self.name = name
        self.country = country
        self.population = population
        self.area = area
        self.last_population_update = last_population_update