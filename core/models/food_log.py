from sqlalchemy.ext.hybrid import hybrid_property
from ..extensions import db
from datetime import datetime
from . import Food

class FoodLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    quantity_g = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.Date, nullable=False, default=datetime.now)


    food_item = db.relationship(Food)

    @hybrid_property
    def format_date(self):
        # date = datetime(self.timestamp)
        # return date
        return self.timestamp

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'food_id': self.food_id,
            'quantity_g': self.quantity_g,
            'timestamp': self.timestamp,
            'food_name': self.food_item.name,
            'vitamin_k_amount': f'{self.food_item.vitamin_k * (self.quantity_g / 100)}μg'
        }