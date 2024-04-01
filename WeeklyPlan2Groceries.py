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
def convert_plan_2_groceries(menu):
    # Create a new dictionary organized by where items might be found in the store
    store_organized_list = {}

    # Iterate over each day in the menu
    for recipe in menu:
        # Iterate over each ingredient in the meal
        print(recipe.ingredients)
        for ingredient in recipe.ingredients:
            # Get the store location of the ingredient
            location = store_locations.get(ingredient, 'other')

            # If the location is not already in the store_organized_list dictionary, add it
            if location not in store_organized_list:
                store_organized_list[location] = []

            # Add the ingredient to the list of items at the store location
            store_organized_list[location].append(ingredient)

    # Print the store_organized_list dictionary
    for location, ingredients in store_organized_list.items():
        print(f"{location}: {', '.join(ingredients)}")

    return store_organized_list

