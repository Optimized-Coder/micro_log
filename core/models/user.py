from ..extensions import db
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    date_of_birth = db.Column(db.Date)
    weight_kg = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    height_cm = db.Column(db.Integer)

    food_logs = db.relationship('FoodLog', backref='user', lazy=True)

    @hybrid_property
    def bmi(self):
        if self.height_cm is not None and self.weight_kg is not None:
            return round(self.weight_kg / ((self.height_cm / 100) ** 2), 2)
        return None