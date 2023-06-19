import csv
import re

from .extensions import db
from .models import Food

def add_food_from_csv(file_path):
    count = 0

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            food = Food(
                name=row['name'],
                serving_size=float(re.sub(r'[^\d.]+', '', row['serving_size'])) if row['serving_size'] else None,
                sodium=float(re.sub(r'[^\d.]+', '', row['sodium'])) if row['sodium'] else None,
                folate=float(re.sub(r'[^\d.]+', '', row['folate'])) if row['folate'] else None,
                folic_acid=float(re.sub(r'[^\d.]+', '', row['folic_acid'])) if row['folic_acid'] else None,
                niacin=float(re.sub(r'[^\d.]+', '', row['niacin'])) if row['niacin'] else None,
                pantothenic_acid=float(re.sub(r'[^\d.]+', '', row['pantothenic_acid'])) if row['pantothenic_acid'] else None,
                riboflavin=float(re.sub(r'[^\d.]+', '', row['riboflavin'])) if row['riboflavin'] else None,
                thiamin=float(re.sub(r'[^\d.]+', '', row['thiamin'])) if row['thiamin'] else None,
                vitamin_a=float(re.sub(r'[^\d.]+', '', row['vitamin_a'])) if row['vitamin_a'] else None,
                vitamin_b12=float(re.sub(r'[^\d.]+', '', row['vitamin_b12'])) if row['vitamin_b12'] else None,
                vitamin_b6=float(re.sub(r'[^\d.]+', '', row['vitamin_b6'])) if row['vitamin_b6'] else None,
                vitamin_c=float(re.sub(r'[^\d.]+', '', row['vitamin_c'])) if row['vitamin_c'] else None,
                vitamin_d=float(re.sub(r'[^\d.]+', '', row['vitamin_d'])) if row['vitamin_d'] else None,
                vitamin_e=float(re.sub(r'[^\d.]+', '', row['vitamin_e'])) if row['vitamin_e'] else None,
                vitamin_k=float(re.sub(r'[^\d.]+', '', row['vitamin_k'])) if row['vitamin_k'] else None,
                calcium=float(re.sub(r'[^\d.]+', '', row['calcium'])) if row['calcium'] else None,
                copper=float(re.sub(r'[^\d.]+', '', row['copper'])) if row['copper'] else None,
                iron=float(re.sub(r'[^\d.]+', '', row['iron'])) if row['iron'] else None,
                magnesium=float(re.sub(r'[^\d.]+', '', row['magnesium'])) if row['magnesium'] else None,
                manganese=float(re.sub(r'[^\d.]+', '', row['manganese'])) if row['manganese'] else None,
                phosphorous=float(re.sub(r'[^\d.]+', '', row['phosphorous'])) if row['phosphorous'] else None,
                potassium=float(re.sub(r'[^\d.]+', '', row['potassium'])) if row['potassium'] else None,
                selenium=float(re.sub(r'[^\d.]+', '', row['selenium'])) if row['selenium'] else None,
                zinc=float(re.sub(r'[^\d.]+', '', row['zinc'])) if row['zinc'] else None
            )

            # Add the food to the session
            db.session.add(food)

            count += 1

            if count % 10 == 0:
                print(f'{count} records added')

        # Commit the session to persist the changes
        db.session.commit()

        print(f'{count} records added. Complete')