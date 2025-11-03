from fastapi import APIRouter
from models.ingredient import Ingredient
from database import ingredients_db

router = APIRouter()

@router.post("/ingredients")
def add_ingredient(ingredient: Ingredient):
    ingredients_db.append(ingredient)
    return {"message": "Ingredient added", "ingredient": ingredient}

@router.get("/ingredients")
def get_ingredients():
    return {"ingredients": ingredients_db}
