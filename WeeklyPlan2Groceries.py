 # The given dictionary
menu = {
    'Friday': (
        {'name': 'Chicken Parmesan', 'ingredients': ['chicken', 'breadcrumbs', 'tomato sauce', 'mozzarella cheese'], 'health_factors': ['low-fat', 'gluten-free'], 'type': 'main'},
        {'name': 'Garlic Knots', 'ingredients': ['bread', 'butter', 'garlic', 'parmesan cheese'], 'health_factors': ['high-fat', 'gluten-free'], 'type': 'side'}
    ),
    'Monday': (
        {'name': 'Spaghetti', 'ingredients': ['pasta', 'tomato sauce', 'ground beef'], 'health_factors': ['high protein', 'low carb'], 'type': 'main'},
        {'name': 'Roasted Vegetables', 'ingredients': ['broccoli', 'carrots', 'potatoes'], 'health_factors': ['high fiber', 'low calorie'], 'type': 'side'}
    ),
    'Wednesday': (
        {'name': 'Grilled Chicken', 'ingredients': ['chicken', 'oil', 'salt'], 'health_factors': ['high protein', 'low fat'], 'type': 'main'},
        {'name': 'Salad', 'ingredients': ['lettuce', 'tomatoes', 'cheese'], 'health_factors': ['low calorie', 'high fiber'], 'type': 'side'}
    )
}

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

# Create a new dictionary organized by where items might be found in the store
store_organized_list = {}

# Iterate over each day in the menu
for day, meals in menu.items():
    # Iterate over each meal in the day's menu
    for meal in meals:
        # Iterate over each ingredient in the meal
        for ingredient in meal['ingredients']:
            # Get the store location of the ingredient
            location = store_locations[ingredient]

            # If the location is not already in the store_organized_list dictionary, add it
            if location not in store_organized_list:
                store_organized_list[location] = []

            # Add the ingredient to the list of items at the store location
            store_organized_list[location].append(ingredient)

# Print the store_organized_list dictionary
for location, ingredients in store_organized_list.items():
    print(f"{location}: {', '.join(ingredients)}")

