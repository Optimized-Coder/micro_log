from flask import Blueprint, jsonify, abort, request
from ..models import Food, Micro
from ..extensions import db
from ..functions import register_user

api = Blueprint('api', __name__, url_prefix='/api')

'''
    GET
'''

@api.route('/food/', methods=['GET'])
def get_all_food():
    '''
    returns: all food items from the database and its nutrient 
    content
    parameters: None
    format: json
    '''
    all_data = Food.query.all()
    
    return jsonify([data.to_dict() for data in all_data])

@api.route('/food/<int:id>', methods=['GET'])
def get_food(id):
    '''
    Returns a single item of food based on id number
    Parameters: food_id
    Format: JSON
    '''
    item = Food.query.get(id)
    if not item:
        abort(404)
    return jsonify(item.to_dict())

@api.route('/get-micros/', methods=['GET'])
def get_all_micros():
    '''
    returns: all micros with info about each nutrient 
    parameters: None
    format: json
    '''
    all_micros = Micro.query.all()

    return jsonify([micro.to_dict() for micro in all_micros])

@api.route('/get-micros/<int:id>', methods=['GET'])
def get_micro(id):
    '''
    Returns a single item of micro based on id number
    Parameters: micro_id
    Format: JSON
    '''
    item = Micro.query.get(id)
    if not item:
        abort(404)
    return jsonify(item.to_dict())

'''
    POST
'''

@api.route('/auth/register/', methods=['POST'])
def register_user():
    '''
    Registers a new user
    Parameters: email, password
    Format: form data
    '''
    user = register_user()

    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())