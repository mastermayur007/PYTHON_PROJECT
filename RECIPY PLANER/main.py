import json

def suggest_recipe(ingredients):
    recipes = {
        "pasta": ["tomato", "cheese", "basil"],
        "salad": ["lettuce", "cucumber", "carrot"],
        "sandwich": ["bread", "lettuce", "tomato"]
    }
    for recipe, req_ingredients in recipes.items():
        if all(item in ingredients for item in req_ingredients):
            return recipe
    return "No matching recipe found."

ingredients = input("Enter your available ingredients separated by commas: ").split(', ')
print(f"Suggested recipe: {suggest_recipe(ingredients)}")