class Meal:
    def __init__(self, name, ingredients, health_factors, type, cook_time, cuisine):
        self.name = name
        self.ingredients = ingredients
        self.health_factors = health_factors
        self.type = type
        self.cook_time = cook_time
        self.cuisine = cuisine

class MealPlan:
    def __init__(self, meals, health_factors, must_cook, must_not_cook, num_dishes):
        self.meals = meals
        self.health_factors = health_factors
        self.must_cook = must_cook
        self.must_not_cook = must_not_cook
        self.num_dishes = num_dishes

    def score_meal(self, meal):
        score = 0
        if meal.name in self.must_cook:
            score += 100
        if meal.name in self.must_not_cook:
            score -= 100
        for factor in self.health_factors:
            if factor in meal.health_factors:
                score += 10
        score -= len(meal.ingredients)  # to prioritize meals with fewer ingredients
        return score

    def generate_plan(self):
        meals.sort(key=self.score_meal, reverse=True)
        plan = []
        for meal in meals:
            if len(plan) >= self.num_dishes:
                break
            if meal.name not in self.must_not_cook:
                plan.append(meal)
        return plan

meals = [
    Meal('Spaghetti', ['pasta', 'tomato sauce', 'ground beef'], ['high protein', 'low carb'], 'main', 20, 'Italian'),
    Meal('Grilled Chicken', ['chicken', 'oil', 'salt'], ['high protein', 'low fat'], 'main', 15, 'American'),
    Meal('Roasted Vegetables', ['broccoli', 'carrots', 'potatoes'], ['high fiber', 'low calorie'], 'side', 30, 'Mediterranean'),
    Meal('Salad', ['lettuce', 'tomatoes', 'cheese'], ['low calorie', 'high fiber'], 'side', 5, 'American'),
    Meal('Chicken Parmesan', ['chicken', 'breadcrumbs', 'tomato sauce', 'mozzarella cheese'], ['low-fat', 'gluten-free'], 'main', 45, 'Italian'),
    Meal('Garlic Knots', ['bread', 'butter', 'garlic', 'parmesan cheese'], ['high-fat', 'gluten-free'], 'side', 60, 'Italian'),
    Meal('Beef Stew', ['beef', 'potatoes', 'carrots', 'onion', 'celery'], ['high protein', 'low carb'], 'main', 120, 'French'),
    Meal('Pan-Seared Salmon', ['salmon', 'lemon', 'butter'], ['high protein', 'low carb'], 'main', 20, 'American'),
]

plan = MealPlan(meals, ['high protein', 'low carb'], ['Pan-Seared Salmon'], ['Garlic Knots'], 3)
print([meal.name for meal in plan.generate_plan()])

