from Hueristic import generate_meal_plan
from Utils.Sheets_communicator import get_recipe_data, update_meal_plan_sheet

def main():
    # Retrieve recipes from the Google Sheet or load from local cache
    recipes = get_recipe_data()

    # Generate a meal plan
    meal_plan = generate_meal_plan(
        7,
        recipes,
        favor_health_factors=['high protein'],
        favor_ingredients=['pasta'],
        must_cook='Spaghetti'
    )

    # Update the meal plan sheet
    update_meal_plan_sheet(meal_plan)

if __name__ == '__main__':
    main()