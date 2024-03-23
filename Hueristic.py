import random

# Sample dish data

def generate_meal_plan(num_meals, dishes, favor_health_factors=None, favor_ingredients=None, must_cook=None):
    meal_plan = {}
    
    # If a specific dish or meal needs to be cooked, add it to the meal plan
    if must_cook:
        meal_plan[1] = next(dish for dish in dishes if dish.name == must_cook)
        num_meals -= 1
    
    # If health factors or ingredients are preferred, sort the dishes accordingly
    if favor_health_factors:
        dishes.sort(key=lambda x: sum(1 for factor in favor_health_factors if factor in x.health_factors), reverse=True)
    if favor_ingredients:
        dishes.sort(key=lambda x: sum(1 for ingredient in favor_ingredients if ingredient in x.ingredients), reverse=True)
    
    # Randomly select dishes to add to the meal plan
    for i in range(2, num_meals + 2):
        meal_plan[i] = random.choice(dishes)
    
    print(meal_plan)
    return meal_plan

# Example usage
