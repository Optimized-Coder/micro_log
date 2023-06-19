from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
admin = Admin()
login_manager = LoginManager()