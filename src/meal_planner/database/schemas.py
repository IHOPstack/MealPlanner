from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Ingredient(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str

class RecipeIngredient(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    amount: Optional[str]
    unit: Optional[str]
    ingredient: Ingredient

class Recipe(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: Optional[str]
    instructions: Optional[str]
    health_factors: Optional[str]
    meal_type: Optional[str]
    cook_mins: Optional[int]
    cuisine: Optional[str]
    ingredients: list[RecipeIngredient] = []


class MealPlanRecipe(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    meal_plan_id: int
    recipe_id: int
    planned_date: Optional[datetime]

class MealPlan(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    recipes: list[MealPlanRecipe]

class GroceryListItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    grocery_list_id: int
    ingredient_id: int
    amount: int
    unit: str
    checked: bool
    ingredient: Ingredient

class GroceryList:
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    items: list[GroceryListItem]
