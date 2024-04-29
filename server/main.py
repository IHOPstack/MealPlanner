from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import models, schemas
from database.database import SessionLocal, engine
from database.crud import get_recipes

from services import Hueristic, WeeklyPlan2Groceries

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




recipes = read_recipes(db=SessionLocal())

this_week = Hueristic.generate_meal_plan(3, recipes, ingredient_preferences="chicken")

WeeklyPlan2Groceries.convert_plan_2_groceries(this_week)