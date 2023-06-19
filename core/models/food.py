from ..extensions import db

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    serving_size = db.Column(db.Float)
    sodium = db.Column(db.Float)
    folate = db.Column(db.Float)
    folic_acid = db.Column(db.Float)
    niacin = db.Column(db.Float)
    pantothenic_acid = db.Column(db.Float)
    riboflavin = db.Column(db.Float)
    thiamin = db.Column(db.Float)
    vitamin_a = db.Column(db.Float)
    vitamin_b12 = db.Column(db.Float)
    vitamin_b6 = db.Column(db.Float)
    vitamin_c = db.Column(db.Float)
    vitamin_d = db.Column(db.Float)
    vitamin_e = db.Column(db.Float)
    vitamin_k = db.Column(db.Float)
    calcium = db.Column(db.Float)
    copper = db.Column(db.Float)
    iron = db.Column(db.Float)
    magnesium = db.Column(db.Float)
    manganese = db.Column(db.Float)
    phosphorous = db.Column(db.Float)
    potassium = db.Column(db.Float)
    selenium = db.Column(db.Float)
    zinc = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'serving_size': self.serving_size,
            'sodium': self.sodium,
            'folate': self.folate,
            'folic acid': self.folic_acid,
            'niacin': self.niacin,
            'pantothenic acid': self.pantothenic_acid,
            'riboflavin': self.riboflavin,
            'thiamine': self.thiamin,
            'vitamin a': self.vitamin_a,
            'vitamin b 12': self.vitamin_b12,
            'vitamin b 6': self.vitamin_b6,
            'vitamin c': self.vitamin_c,
            'vitamin d': self.vitamin_d,
            'vitamin e': self.vitamin_e,
            'vitamin k': self.vitamin_k,
            'calcium': self.calcium,
            'copper': self.copper,
            'iron': self.iron,
            'magnesium': self.magnesium,
            'manganese': self.manganese,
            'phosphorus': self.phosphorous,
            'potassium': self.potassium,
            'selenium': self.selenium,
            'zinc': self.zinc
        }
