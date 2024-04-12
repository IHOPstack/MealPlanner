from Hueristic import generate_meal_plan
from Utils.Sheets_communicator import get_recipe_data, update_meal_plan_sheet, update_grocery_note
from WeeklyPlan2Groceries import convert_plan_2_groceries

def main():
    # Retrieve recipes from the Google Sheet or load from local cache
    recipes = get_recipe_data()

    # Generate a meal plan
    meal_plan = generate_meal_plan(
        7,
        recipes,
        health_preferences=['high protein'],
        ingredient_preferences=['brussel sprouts'],
        must_cook=['Arrabiata']
    )

    # Update the meal plan sheet
    update_meal_plan_sheet(meal_plan)

    # Create grocery list
    groceries = convert_plan_2_groceries(meal_plan)

    # Push grocery list to Keep
    update_grocery_note(groceries)


if __name__ == '__main__':
    main()