from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from googleapiclient.discovery import build
from recipe import Recipe
import Hueristic

# Replace with the path to your JSON key file
KEY_FILE = 'Skeleton_closet/winter-cocoa-418006-70f14d7c8e87.json'

# Replace with the ID of your Google Sheet
SHEET_ID = '1ZANX4fge4qNNlXchirwgIaCUeLrIuNXU-t3VpvT1C80'

# Replace with the name of the sheet within your Google Sheet
SHEET_NAME = 'recipes'

# Replace with the range of cells containing your data
RANGE = 'A1:Z100'  # Adjust the range as needed

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
                name=row[1],
                ingredients=row[2].split(', '),
                health_factors= row[3],
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
    meal_plan = [['Day', 'Recipe'], *[[day, recipe.name] for day, recipe in meal_plan.items()]]

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