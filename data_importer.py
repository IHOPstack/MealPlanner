from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from sqlalchemy.orm import sessionmaker
from database import Recipe, Ingredient, RecipeIngredient, engine

def import_data_from_sheets():
    # Load credentials and create a connection to the Google Sheets API
    creds = Credentials.from_service_account_file('Skeleton_closet/winter-cocoa-418006-70f14d7c8e87.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])
    sheets_service = build('sheets', 'v4', credentials=creds)

    # Retrieve the data from your Google Sheets
    sheet_id = '1ZANX4fge4qNNlXchirwgIaCUeLrIuNXU-t3VpvT1C80'
    range_name = 'Sheet1!A1:Z'
    result = sheets_service.spreadsheets().values().get(spreadsheetId=sheet_id, range=range_name).execute()
    data = result.get('values', [])

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Process the data and populate the database tables
    for row in data[1:]:  # Skip the header row
        recipe_name = row[1]
        ingredient_names = row[2].split(', ')
        health_factors_string = row[3]
        meal_type_string = row[4]
        cook_time_int = int(row[5])
        cuisine_string = row[6]

        # Extract other relevant data from the row

        # Create or retrieve the recipe
        recipe = session.query(Recipe).filter_by(name=recipe_name).first()
        if not recipe:
            recipe = Recipe(name=recipe_name, health_factors=health_factors_string, meal_type=meal_type_string, cook_time=cook_time_int, cuisine=cuisine_string)
            session.add(recipe)

        # Create or retrieve the ingredients and associate them with the recipe
        for ingredient_name in ingredient_names:
            ingredient = session.query(Ingredient).filter_by(name=ingredient_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ingredient_name)
                session.add(ingredient)

            recipe_ingredient = RecipeIngredient(recipe=recipe, ingredient=ingredient)
            session.add(recipe_ingredient)

    # Commit the changes to the database
    session.commit()

if __name__ == '__main__':
    import_data_from_sheets()
