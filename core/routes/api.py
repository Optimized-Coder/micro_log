from flask import Blueprint, jsonify
from ..models import Food, Micro

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/get-foods/')
def get_all_food():
    '''
    returns: all food items from the database and its nutrient 
    content
    parameters: None
    format: json
    '''
    all_data = Food.query.all()
    
    return jsonify([data.to_dict() for data in all_data])

@api.route('/get-micros/')
def get_all_micros():
    '''
    returns: all micros with info about each nutrient 
    parameters: None
    format: json
    '''
    all_micros = Micro.query.all()

    return jsonify([micro.to_dict() for micro in all_micros])