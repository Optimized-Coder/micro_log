from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required

from ..models import Food, FoodLog
from ..extensions import db
from ..functions import get_date, get_logs_by_date

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@login_required
def index():
    return f"Hello, {current_user.name}"


@main.route('/add-log/', methods=['GET'])
@login_required
def add_log():
    '''
    method: GET
    description: searches a food query 
    returns: all foods that match the query
      -links to post method which takes in the id
        - e.g. http://domain/add-log/id/quantity
    '''
    food_query = request.form.get('food_query')
    food_results = Food.query.filter(Food.name.like(f'%{food_query}%')).all()
    quantity = request.form.get('quantity')

    return [f'href="https://DOMAIN/add-log/{food.id}/{quantity}"' for food in food_results]

@main.route('/add-log/<int:food_id>/', methods=['POST'])
@login_required
def add_log_post(food_id):
    '''
    method: POST
    description: adds a food log to the database
    parameters: food_id linked from the previous GET route
    '''
    user_id = current_user.id
    food_id = food_id
    quantity_g = request.args.get('quantity_g')

    new_log = FoodLog(user_id=user_id, food_id=food_id, quantity_g=quantity_g)

    db.session.add(new_log)
    db.session.commit()

    return f'Log Added: {new_log.food_item.name}, {new_log.quantity_g}, {new_log.timestamp}'


@main.route('/logs/', methods=['GET'])
@login_required
def get_logs():
    user_id = current_user.id
    logs = FoodLog.query.filter(FoodLog.user_id == user_id).all()
    
    return jsonify([log.to_dict() for log in logs])

@main.route('/logs/<int:user_id>/today/')
@login_required
def get_logs_today(user_id):
    user_id = current_user.id
    year, month, day = get_date()
    print(year, month, day)
    logs = FoodLog.query.filter(
        user_id == user_id and\
              FoodLog.timestamp.like(f'{year}-{month}-{day}')
    ).all()


    return jsonify([log.to_dict() for log in logs])

@main.route('/logs/<int:user_id>/')
@login_required
def get_past_logs(user_id):
    logs = get_logs_by_date()

    return jsonify([log.to_dict() for log in logs])