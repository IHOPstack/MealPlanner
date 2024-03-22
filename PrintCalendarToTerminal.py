import click

# Define a function to print the meal plan
def print_meal_plan(meal_plan):
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    sorted_meal_plan = dict(sorted(meal_plan.items(), key=lambda x: weekdays.index(x[0])))
    for day, meals in sorted_meal_plan.items():
        click.secho(day, fg='blue')  # Print the day in blue
        for meal in meals:
            click.secho(meal['name'], fg='green')  # Print the meal name in green
            click.echo('Ingredients: ' + ', '.join(meal['ingredients']))  # Print the ingredients
            click.echo('Health factors: ' + ', '.join(meal['health_factors']))  # Print the health factors
            click.echo('Type: ' + meal['type'])  # Print the meal type
            click.echo('')

# Your example input
meal_plan = {'Friday': ({'name': 'Chicken Parmesan', 'ingredients': ['chicken', 'breadcrumbs', 'tomato sauce', 'mozzarella cheese'], 'health_factors': ['low-fat', 'gluten-free'], 'type': 'main'}, {'name': 'Garlic Knots', 'ingredients': ['bread', 'butter', 'garlic', 'parmesan cheese'], 'health_factors': ['high-fat', 'gluten-free'], 'type': 'side'}), 'Monday': ({'name': 'Spaghetti', 'ingredients': ['pasta', 'tomato sauce', 'ground beef'], 'health_factors': ['high protein', 'low carb'], 'type': 'main'}, {'name': 'Roasted Vegetables', 'ingredients': ['broccoli', 'carrots', 'potatoes'], 'health_factors': ['high fiber', 'low calorie'], 'type': 'side'}), 'Wednesday': ({'name': 'Grilled Chicken', 'ingredients': ['chicken', 'oil', 'salt'], 'health_factors': ['high protein', 'low fat'], 'type': 'main'}, {'name': 'Salad', 'ingredients': ['lettuce', 'tomatoes', 'cheese'], 'health_factors': ['low calorie', 'high fiber'], 'type': 'side'})}

print_meal_plan(meal_plan)

