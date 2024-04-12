import random

def create_meal_plan(dishes, meals_per_week, days_off=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meal_plan = {}

    # Remove days off from the list of days
    if days_off:
        for day in days_off:
            days_of_week.remove(day)

    # Randomly select main dishes
    main_dishes = random.sample([dish for dish in dishes if dish['type'] == 'main'], meals_per_week)

    # Randomly select side dishes
    side_dishes = random.sample([dish for dish in dishes if dish['type'] == 'side'], meals_per_week)

    # Pair main dishes with side dishes
    meals = list(zip(main_dishes, side_dishes))

    # Assign meals to days
    for i in range(meals_per_week):
        meal_day = int(i/meals_per_week * len(days_of_week)) -1
        meal_plan[days_of_week[meal_day]] = meals[i % len(meals)]

    return meal_plan

# Example usage
dishes = [
    {'name': 'Spaghetti', 'ingredients': ['pasta', 'tomato sauce', 'ground beef'], 'health_factors': ['high protein', 'low carb'], 'type': 'main', 'cook time': 20},
    {'name': 'Grilled Chicken', 'ingredients': ['chicken', 'oil', 'salt'], 'health_factors': ['high protein', 'low fat'], 'type': 'main', 'cook time': 15},
    {'name': 'Roasted Vegetables', 'ingredients': ['broccoli', 'carrots', 'potatoes'], 'health_factors': ['high fiber', 'low calorie'], 'type': 'side', 'cook time': 30},
    {'name': 'Salad', 'ingredients': ['lettuce', 'tomatoes', 'cheese'], 'health_factors': ['low calorie', 'high fiber'], 'type': 'side', 'cook time': 5},
    {'name': 'Chicken Parmesan', 'ingredients': ['chicken', 'breadcrumbs', 'tomato sauce', 'mozzarella cheese'], 'health_factors': ['low-fat', 'gluten-free'], 'type': 'main', 'cook time': 45},
    {'name': 'Garlic Knots', 'ingredients': ['bread', 'butter', 'garlic', 'parmesan cheese'], 'health_factors': ['high-fat', 'gluten-free'], 'type': 'side', 'cook time': 60}
]

meal_plan = create_meal_plan(dishes, 3, ['Saturday', 'Sunday'])
print(meal_plan)
