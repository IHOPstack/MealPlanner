from database import models
from database.database import SessionLocal

from Hueristic import generate_meal_plan

def test_generate_meal_plan():
    db = SessionLocal()
    recipes = db.query(models.Recipe).all()
    this_week = generate_meal_plan(3, recipes)
    print(this_week)
    db.close()

test_generate_meal_plan()
