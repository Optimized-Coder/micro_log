from flask import Flask, jsonify
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .functions import add_food_from_csv
from .extensions import db, migrate, login_manager
from .models import Food, Micro, User, FoodLog

def create_app():
    ''' factory function that is the main entry for the app '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kdjffnvnfrv'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Replace with your database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    admin = Admin(app, name='micro_app', template_mode='bootstrap3')
    login_manager.init_app(app)

    # setup flask admin 
    admin.add_view(ModelView(Micro, db.session))
    admin.add_view(ModelView(Food, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(FoodLog, db.session))

    # flask login setup
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    login_manager.login_view = "auth.login"

    # register blueprints
    from .routes import api_bp, auth_bp
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    @app.route('/add_foods')
    def add_foods():
        '''
        follow this route to add data from csv to data.db file
        '''
        add_food_from_csv('./nutrition.csv')

        return 'Foods added successfully!'


    return app