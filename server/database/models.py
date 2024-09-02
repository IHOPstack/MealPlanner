from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    instructions = Column(Text)
    health_factors = Column(String(255))
    meal_type = Column(String(50))
    cook_mins = Column(Integer)
    cuisine = Column(String(50))
    ingredients = relationship('RecipeIngredient', back_populates='recipe')
    meal_plans = relationship('MealPlan', secondary='meal_plan_recipes', back_populates='recipes')

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    amount = Column(String(50))
    unit = Column(String(50))
    recipe = relationship('Recipe', back_populates='ingredients')
    ingredient = relationship('Ingredient')

class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    recipes = relationship('Recipe', secondary='meal_plan_recipes', back_populates='meal_plans')

class MealPlanRecipe(Base):
    __tablename__ = 'meal_plan_recipes'
    meal_plan_id = Column(Integer, ForeignKey('meal_plans.id'), primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    planned_date = Column(DateTime)

class GroceryList(Base):
    __tablename__ = 'grocery_lists'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(255), nullable=False)
    items = relationship('GroceryListItem', back_populates='grocery_list')

class GroceryListItem(Base):
    __tablename__ = 'grocery_list_items'
    id = Column(Integer, primary_key=True)
    grocery_list_id = Column(Integer, ForeignKey('grocery_lists.id'))
    ingredient_id = (Column(Integer, ForeignKey('ingredients.id')))
    amount = Column(String(50))
    unit = Column(String(50))
    checked = Column(Boolean, default=False)
    ingredient = relationship('Ingredient')
    grocery_list = relationship('GroceryList', back_populates='items')