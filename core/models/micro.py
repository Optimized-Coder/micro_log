from ..extensions import db

class Micro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    male_minimum = db.Column(db.Float)
    female_minimum = db.Column(db.Float)
    unit = db.Column(db.String(5))

    def __repr__(self):
        return f'{self.id}: {self.name}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'male_minimum': self.male_minimum,
            'female_minimum': self.female_minimum,
            'unit': self.unit
        }