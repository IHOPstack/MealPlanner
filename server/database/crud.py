from sqlalchemy.orm import Session

from . import models, schemas

# Recipes CRUD
def get_recipes(db: Session, skip: int = 0, limit: int = 100) -> list[models.Recipe]:
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def get_recipe_by_id(db: Session, recipe_id: int) -> models.Recipe | None:
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def create_recpie(db: Session, recipe: schemas.Recipe) -> models.Recipe:
    db_recipe = models.Recipe(id=recipe.id, name=recipe.name, description=recipe.description, instructions=recipe.instructions, health_factors=recipe.health_factors, meal_type=recipe.meal_type, cook_mins=recipe.cook_mins, cuisine=recipe.cuisine,ingredients=recipe.ingredients)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete_recipe(db: Session, recipe: schemas.Recipe) -> None:
    db_recipe = get_recipe_by_id(db, recipe.id)
    db.delete(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return None

def update_recipe(db: Session, recipe: schemas.Recipe) -> models.Recipe:
    db_recipe = get_recipe_by_id(db, recipe.id)
    db.query(models.Recipe).filter(models.Recipe.id == db_recipe.id).update(db_recipe.__dict__)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe