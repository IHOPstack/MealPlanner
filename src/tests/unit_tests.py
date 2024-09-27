from meal_planner.database import models
from meal_planner.database.db import SessionLocal
from meal_planner.database.schemas import Recipe
from meal_planner.database.crud import get_recipes

import unittest
from unittest.mock import patch

from meal_planner.services.Hueristic import generate_meal_plan

class TestGenerateMealPlan(unittest.TestCase):
    recipes = get_recipes(SessionLocal())

    def test_meal_plan_length(self):
        num_meals = 5
        meal_plan = generate_meal_plan(num_meals, self.recipes)
        self.assertEqual(len(meal_plan), num_meals)

    def test_meal_plan_type(self):
        recipes = self.recipes
        num_meals = 5
        meal_plan = generate_meal_plan(num_meals, recipes)
        self.assertTrue(all(recipe.meal_type == 'main' for recipe in meal_plan))

    def test_meal_plan_uniqueness(self):
        recipes = self.recipes
        num_meals = 5
        meal_plan = generate_meal_plan(num_meals, recipes)
        self.assertEqual(len(meal_plan), len(set(meal_plan)))

    def test_health_preferences(self):
        recipes = self.recipes
        num_meals = 5
        health_preferences = ['low_fat']
        meal_plan = generate_meal_plan(num_meals, recipes, health_preferences=health_preferences)
        self.assertTrue(all(any(health_factor in health_preferences for health_factor in recipe.health_factors) for recipe in meal_plan))

    def test_ingredient_preferences(self):
        recipes = self.recipes
        num_meals = 5
        ingredient_preferences = ['chicken']
        meal_plan = generate_meal_plan(num_meals, recipes, ingredient_preferences=ingredient_preferences)
        self.assertTrue(all(any(ingredient in ingredient_preferences for ingredient in recipe.ingredients) for recipe in meal_plan))

    def test_must_cook_recipes(self):
        recipes = self.recipes
        num_meals = 5
        must_cook = ['Adobo Chicken']
        meal_plan = generate_meal_plan(num_meals, recipes, must_cook=must_cook)
        self.assertIn(recipes[0], meal_plan)

    def test_randomness(self):
        recipes = self.recipes
        num_meals = 5
        meal_plan1 = generate_meal_plan(num_meals, recipes)
        meal_plan2 = generate_meal_plan(num_meals, recipes)
        self.assertNotEqual(meal_plan1, meal_plan2)

if __name__ == '__main__':
    unittest.main()

