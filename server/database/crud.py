from sqlalchemy.orm import Session
from . import models, schemas

def get_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recipe).offset(skip).limit(limit).all()
