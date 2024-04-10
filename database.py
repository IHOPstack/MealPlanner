from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    instructions = Column(Text)
    health_factors = Column(String(255))
    meal_type = Column(String(50))
    cook_mins = Column(Integer)
    cuisine = Column(String(50))
    ingredients = relationship('RecipeIngredient', back_populates='recipe')

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    amount = Column(String(50))
    unit = Column(String(50))
    recipe = relationship('Recipe', back_populates='ingredients')
    ingredient = relationship('Ingredient')

# Define the MealPlan model
class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    recipes = relationship('Recipe', secondary='meal_plan_recipes', back_populates='meal_plans')

# Define the MealPlanRecipe model (many-to-many relationship)
class MealPlanRecipe(Base):
    __tablename__ = 'meal_plan_recipes'
    meal_plan_id = Column(Integer, ForeignKey('meal_plans.id'), primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    planned_date = Column(DateTime)

class GroceryList(Base):
    __tablename__ = 'gorcery_lists'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

class GroceryListItem(Base):
    __tablename__ = 'gorcery_list_items'
    id = Column(Integer, primary_key=True)
    grocery_list_id = Column(Integer, ForeignKey('grocery_lists.id'), primary_key=True)
    ingredient_id = (Column(Integer, ForeignKey('ingredients.id'), primary_key=True))
    amount = Column(String(50))
    unit = Column(String(50))
    checked = False


# Create the database connection
engine = create_engine('mysql+pymysql://newuser:newpassword@localhost/meal_planner')
Base.metadata.create_all(engine)
