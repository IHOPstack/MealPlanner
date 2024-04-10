from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from googleapiclient.discovery import build
from recipe import Recipe

KEY_FILE = 'Skeleton_closet/winter-cocoa-418006-70f14d7c8e87.json'
SHEET_ID = '1ZANX4fge4qNNlXchirwgIaCUeLrIuNXU-t3VpvT1C80'
SHEET_NAME = 'recipes'
KEEP_ID = '19CJDWVk1Tq7gNxpzfQAWLliIzrD-DPbfhCzfmNQeeJywNuj8lwIt-mKi0hWnT--E7NTV'
RANGE = 'A1:Z100'  # Adjust the range as needed

from sqlalchemy.orm import sessionmaker
from database import Recipe, Ingredient, RecipeIngredient, engine

def import_data_from_sheets():
    # Load credentials and create a connection to the Google Sheets API
    creds = ServiceAccountCredentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
    sheets_service = build('sheets', 'v4', credentials=creds)

    # Retrieve the data from your Google Sheets
    result = sheets_service.spreadsheets().values().get(spreadsheetId=SHEET_ID, range=RANGE).execute()
    data = result.get('values', [])

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Process the data and populate the database tables
    for row in data[1:]:  # Skip the header row
        recipe_name = row[0]
        ingredient_names = row[1].split(', ')
        # Extract other relevant data from the row

        # Create or retrieve the recipe
        recipe = session.query(Recipe).filter_by(name=recipe_name).first()
        if not recipe:
            recipe = Recipe(name=recipe_name)
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




def get_recipe_data():
    # Load credentials from the service account JSON key file
    creds = ServiceAccountCredentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Create a connection to the Google Sheets API
    service = build('sheets', 'v4', credentials=creds)

    # Retrieve the data from the specified sheet and range
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=f"{SHEET_NAME}!{RANGE}").execute()
    data = result.get('values', [])

    # Process the retrieved data
    recipes = []
    for row in data[1:]:  # Skip the header row
        if row[7] == 'TRUE':
            recipe = Recipe(
                name= row[1],
                ingredients= row[2].split(', '),
                health_factors= list(row[3]),
                type= row[4],
                cook_time= int(row[5]),
                cuisine= row[6]
            )
            recipes.append(recipe)

    # Print the recipes    
    return recipes
    


def update_meal_plan_sheet(meal_plan):
    # Load credentials from the service account JSON key file
    creds = ServiceAccountCredentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Create a connection to the Google Sheets API
    service = build('sheets', 'v4', credentials=creds)

    # Assuming meal_plan is a 2D list containing the meal plan data
    sheet_name = 'meal plan'
    range_name = f"{sheet_name}!B2"

    #Convert meal_plan dictionary to a 2D list
    meal_plan = [['Day', 'Recipe'], *[[day + 1, recipe.name] for day, recipe in enumerate(meal_plan)]]

    # Write the meal plan data to the sheet
    print(meal_plan)
    body = {
        'values': meal_plan
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

    # Get the sheet ID dynamically
    sheet_metadata = service.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
    sheets = sheet_metadata.get('sheets', '')
    sheet_id_int = next((sheet['properties']['sheetId'] for sheet in sheets if sheet['properties']['title'] == sheet_name), None)
    
    if sheet_id_int is None:
        raise ValueError(f"Sheet '{sheet_name}' not found in the Google Sheet.")


    # Apply formatting to the sheet
    requests = [
        {
            "updateCells": {
                "range": {
                    "sheetId": sheet_id_int,
                    "startRowIndex": 0,
                    "endRowIndex": len(meal_plan),
                    "startColumnIndex": 0,
                    "endColumnIndex": len(meal_plan[0])
                },
                "rows": [
                    {
                        "values": [
                            {
                                "userEnteredFormat": {
                                    "backgroundColor": {
                                        "red": 1.0,
                                        "green": 0.8,
                                        "blue": 0.8
                                    },
                                    "textFormat": {
                                        "bold": True
                                    }
                                }
                            } for _ in range(len(meal_plan[0]))
                        ]
                    } for _ in range(len(meal_plan))
                ],
                "fields": "userEnteredFormat(backgroundColor,textFormat)"
            }
        }
    ]

    body = {
        'requests': requests
    }
    response = service.spreadsheets().batchUpdate(
        spreadsheetId=SHEET_ID,
        body=body
    ).execute()

    return(True)

def update_grocery_note(groceries):
    # Load credentials from the service account JSON key file
    creds = ServiceAccountCredentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/keep'])
    
    # Establish connection with Keep API
    keep_service = build('keep', 'v1', credentials=creds)

    text = ''
    for location, ingredients in groceries.items():
        text += f"{location}:\n"
        for ingredient in ingredients:
            text += f"- [ ] {ingredient}\n"
        text += "\n"

    note_name = f'notes/{KEEP_ID}'
    note = keep_service.notes().get(name=note_name).execute()
    note['textContent'] = text
    updated_note = keep_service.notes().update(name=note_name, body=note).execute()
    print(f"Note updated: {updated_note['title']}")
