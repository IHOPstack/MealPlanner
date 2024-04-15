from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List


class Recipe(BaseModel):
    name: str
    factor: List[str]
    ingredients: List[str]


class MealPlanRequest(BaseModel):
    num_meals: int
    recipes: List[Recipe]
    health_preferences: Optional[List[str]]
    ingredient_preferences: Optional[List[str]]
    must_cook: Optional[List[str]]


app = FastAPI()


@app.post("/meal-plan", response_model=MealPlanRequest)
def create_meal_plan(request: MealPlanRequest):
    return request


# Example usage
request = MealPlanRequest(
    num_meals=5,
    recipes=[
        Recipe(name="Recipe 1", factor=["healthy", "italian"], ingredients=["pasta", "tomato sauce"]),
        Recipe(name="Recipe 2", factor=["unhealthy", "mexican"], ingredients=["tortilla", "chicken"])
    ],
    health_preferences=["healthy"],
    ingredient_preferences=["chicken"],
    must_cook=["Recipe 1"]
)


response = app.post("/meal-plan", json=request.dict())


assert response.status_code == 200
assert response.json()["num_meals"] == 5
assert response.json()["recipes"][0]["name"] == "Recipe 1"
assert response.json()["health_preferences"] == ["healthy"]
assert response.json()["ingredient_preferences"] == ["chicken"]
assert response.json()["must_cook"] == ["Recipe 1"]


