from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from googleapiclient.discovery import build
import Hueristic

# Replace with the path to your JSON key file
KEY_FILE = 'winter-cocoa-418006-70f14d7c8e87.json'

# Replace with the ID of your Google Sheet
SHEET_ID = '1ZANX4fge4qNNlXchirwgIaCUeLrIuNXU-t3VpvT1C80'

# Replace with the name of the sheet within your Google Sheet
SHEET_NAME = 'recipes'

# Replace with the range of cells containing your data
RANGE = 'A1:Z100'  # Adjust the range as needed

def main():
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
        recipe = {
            'name': row[1],
            'ingredients': row[2].split(', '),
            'health tags': row[3],
            'type': row[4],
            'cook time': int(row[5]),
            'cuisine': row[6]
        }
        recipes.append(recipe)

    # Print the recipes
    for recipe in recipes:
        for key, value in recipe.items():
            print(f'{key}: {value}')
        print()
    
    return recipes


if __name__ == '__main__':
    main()
