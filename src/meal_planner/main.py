from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from meal_planner.database import models, schemas
from meal_planner.database.db import SessionLocal, engine
from meal_planner.database.crud import get_recipes

from meal_planner.services import Hueristic, WeeklyPlan2Groceries

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/recipes/", response_model=list[schemas.Recipe])
def read_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recipes = get_recipes(db, skip=skip, limit=limit)
    return recipes

@app.post("/meal-plan/")
def generate_meal_plan(num_meals: int, ingredient_preferences: str, must_cook: list[str], db: Session = Depends(get_db)):
    recipes = get_recipes(db)
    meal_plan = Hueristic.generate_meal_plan(num_meals, recipes, ingredient_preferences=ingredient_preferences, must_cook=['Chicken Adobo'])
    return meal_plan

@app.post("/groceries/")
def convert_to_groceries(meal_plan: schemas.MealPlan):
    groceries = WeeklyPlan2Groceries.convert_plan_2_groceries(meal_plan)
    return groceries