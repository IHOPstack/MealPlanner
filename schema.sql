-- Create the recipes table
CREATE TABLE recipes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  instructions TEXT,
  health_factors VARCHAR(255),
  meal_type VARCHAR(50),
  cook_mins INT,
  cuisine VARCHAR(50)
);

-- Create the ingredients table
CREATE TABLE ingredients (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Create the recipe_ingredients table (many-to-many relationship)
CREATE TABLE recipe_ingredients (
  recipe_id INT,
  ingredient_id INT,
  amount VARCHAR(50),
  unit VARCHAR(50),
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (recipe_id) REFERENCES recipes(id),
  FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
);

-- Create the meal_plans table
CREATE TABLE meal_plans (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  start_date DATE,
  end_date DATE
);

-- Create the meal_plan_recipes table (many-to-many relationship)
CREATE TABLE meal_plan_recipes (
  meal_plan_id INT,
  recipe_id INT,
  planned_date DATE,
  PRIMARY KEY (meal_plan_id, recipe_id),
  FOREIGN KEY (meal_plan_id) REFERENCES meal_plans(id),
  FOREIGN KEY (recipe_id) REFERENCES recipes(id)
);

-- Create the grocery_lists table
CREATE TABLE grocery_lists (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

-- Create the grocery_list_items table
CREATE TABLE grocery_list_items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  grocery_list_id INT,
  ingredient_id INT,
  amount VARCHAR(50),
  unit VARCHAR(50),
  checked BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (grocery_list_id) REFERENCES grocery_lists(id),
  FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
);
