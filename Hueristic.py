import random

def generate_meal_plan(num_meals, recipes, favor_health_factors=None, favor_ingredients=None, must_cook=None):
    meal_plan = {}

    # If a specific dish or meal needs to be cooked, add it to the meal plan
    if must_cook:
        matching_recipes = [recipe for recipe in recipes if recipe.name.lower() == must_cook.lower()]
        if matching_recipes:
            meal_plan[1] = matching_recipes[0]
            num_meals -= 1
        else:
            print(f"No recipe found for '{must_cook}'. Skipping it.")

    # Calculate scores for each recipe based on favored health factors and ingredients
    for recipe in recipes:
        recipe.score = 0
        if favor_health_factors:
            recipe.score += sum(1 for factor in favor_health_factors if factor in recipe.health_factors)
        if favor_ingredients:
            recipe.score += sum(1 for ingredient in favor_ingredients if ingredient in recipe.ingredients)

    # Sort recipes based on scores in descending order
    sorted_recipes = sorted(recipes, key=lambda x: x.score, reverse=True)

    # Randomly select recipes with higher scores to add to the meal plan
    for i in range(2, num_meals + 2):
        if sorted_recipes:
            recipe = random.choices(sorted_recipes, weights=[r.score for r in sorted_recipes])[0]
            meal_plan[i] = recipe
            sorted_recipes.remove(recipe)
        else:
            break

    return meal_plan
