import requests

from meal_planner.skeleton_closet import USDA_API_KEY
from meal_planner.skeleton_closet import USDA_API_URL

def get_ingredient_data(ingredient_name):
    params = {
        'api_key': USDA_API_KEY,
        'query': ingredient_name,
        'pageSize': 1,
        'requireAllWords': True
    }
    response = requests.get(USDA_API_URL, params=params)
    data = response.json()

    if data['totalHits'] > 0:
        food_data = data['foods'][0]
        nutrient_data = {
            'protein_content': None,
            'fat_content': None,
            'carbohydrate_content': None
            # Add other nutritional fields as needed
        }
        for nutrient in food_data['foodNutrients']:
            if nutrient['nutrientName'] == 'Protein':
                nutrient_data['protein_content'] = nutrient['value']
            elif nutrient['nutrientName'] == 'Total lipid (fat)':
                nutrient_data['fat_content'] = nutrient['value']
            elif nutrient['nutrientName'] == 'Carbohydrate, by difference':
                nutrient_data['carbohydrate_content'] = nutrient['value']
            # Add other nutrient mappings as needed
        return nutrient_data
    else:
        return None
    
print(get_ingredient_data('broccoli'))

# from database.models import Ingredient
# from database.database import SessionLocal
# from usda_api import get_ingredient_data

# def update_ingredient_data():
#     db = SessionLocal()
#     ingredients = db.query(Ingredient).all()
    
#     for ingredient in ingredients:
#         nutrient_data = get_ingredient_data(ingredient.name)
#         if nutrient_data:
#             ingredient.protein_content = nutrient_data['protein_content']
#             ingredient.fat_content = nutrient_data['fat_content']
#             ingredient.carbohydrate_content = nutrient_data['carbohydrate_content']
#             # Update other nutritional fields as needed
    
#     db.commit()
#     db.close()

# # Update nutritional data for existing ingredients
# update_ingredient_data()

# # Update nutritional data when a new ingredient is added
# def create_ingredient(ingredient_data):
#     db = SessionLocal()
#     ingredient = Ingredient(**ingredient_data)
#     db.add(ingredient)
#     db.commit()
    
#     nutrient_data = get_ingredient_data(ingredient.name)
#     if nutrient_data:
#         ingredient.protein_content = nutrient_data['protein_content']
#         ingredient.fat_content = nutrient_data['fat_content']
#         ingredient.carbohydrate_content = nutrient_data['carbohydrate_content']
#         # Update other nutritional fields as needed
#         db.commit()
    
#     db.close()
