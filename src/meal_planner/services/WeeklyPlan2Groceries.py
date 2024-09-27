from meal_planner.database.schemas import Recipe
from collections import defaultdict

# Dictionary of where each grocery item might be found in the store
store_locations = {
    'chicken': 'Meat Department',
    'breadcrumbs': 'Baking Supplies',
    'tomato sauce': 'Pantry',
    'mozzarella cheese': 'Dairy',
    'bread': 'Bakery',
    'butter': 'Dairy',
    'garlic': 'Produce',
    'parmesan cheese': 'Dairy',
    'pasta': 'Pantry',
    'ground beef': 'Meat Department',
    'broccoli': 'Produce',
    'carrots': 'Produce',
    'potatoes': 'Produce',
    'lettuce': 'Produce',
    'tomatoes': 'Produce',
    'cheese': 'Dairy',
    'oil': 'Pantry',
    'salt': 'Pantry'
}
def convert_plan_2_groceries(menu: list[Recipe]):
    # Create a new dictionary organized by where items might be found in the store
    store_organized_list = defaultdict(set)

    # Iterate over each day in the menu
    for recipe in menu:
        # Iterate over each ingredient in the meal
        for ingredient in recipe.ingredients:
            # Get the store location of the ingredient
            location = store_locations.get(ingredient, 'other')
            # Add the ingredient to the list of items at the store location
            store_organized_list[location].add(ingredient)

    # Print the store_organized_list dictionary
    for location, ingredients in store_organized_list.items():
        print(f"{location}: {', '.join([ingredient.ingredient.name for ingredient in ingredients])}")

    return store_organized_list

