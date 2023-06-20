from ..extensions import db
from datetime import datetime
from . import Food

class FoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    quantity_g = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    food_item = db.relationship(Food)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'food_id': self.food_id,
            'quantity_g': self.quantity_g,
            'timestamp': self.timestamp
        }