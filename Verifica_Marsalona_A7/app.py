from flask import Flask, request, jsonify
from models import db, City
from config import Config
from datetime import datetime