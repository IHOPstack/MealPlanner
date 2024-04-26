from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Ingredient(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class RecipeIngredient(BaseModel):
    amount: Optional[str]
    unit: Optional[str]
    ingredient: Ingredient
    class Config:
        orm_mode = True

class Recipe(BaseModel):
    id: int
    name: str
    description: Optional[str]
    instructions: Optional[str]
    health_factors: Optional[str]
    meal_type: Optional[str]
    cook_mins: Optional[int]
    cuisine: Optional[str]
    ingredients: list[RecipeIngredient] = []
    class Config:
        orm_mode = True

class MealPlanRecipe(BaseModel):
    meal_plan_id: int
    recipe_id: int
    planned_date: Optional[datetime]
    class Config:
        orm_mode = True

class MealPlan(BaseModel):
    id: int
    name: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    recipes: list[MealPlanRecipe]
    class Config:
        orm_mode = True

class GroceryListItem(BaseModel):
    id: int
    grocery_list_id: int
    ingredient_id: int
    amount: int
    unit: str
    checked: bool
    ingredient: Ingredient
    class config:
        orm_mode = True

class GroceryList:
    id: int
    name: str
    items: list[GroceryListItem]
    class config:
        orm_mode = True