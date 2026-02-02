from typing import List
from data.ingredient_pool import INGREDIENT_POOL
from models.ingredient import Ingredient


def get_unlocked_ingredients(stage: int) -> List[Ingredient]:
    unlocked_ingredients = []

    for ingredient in INGREDIENT_POOL:
        if stage >= ingredient.unlock_stage:
            unlocked_ingredients.append(ingredient)

    return unlocked_ingredients


def is_ingredient_unlocked(ingredient_key: str, stage: int) -> bool:
    for ingredient in INGREDIENT_POOL:
        if ingredient.key == ingredient_key:
            return stage >= ingredient.unlock_stage
    return False


def get_ingredient_by_key(ingredient_key: str) -> Ingredient | None:
    for ingredient in INGREDIENT_POOL:
        if ingredient.key == ingredient_key:
            return ingredient
    return None


def get_ingredient_name(ingredient_key: str) -> str:
    ingredient = get_ingredient_by_key(ingredient_key)
    return ingredient.name if ingredient else ingredient_key


def get_ingredient_cost(ingredient_key: str) -> int:
    ingredient = get_ingredient_by_key(ingredient_key)
    return ingredient.base_cost if ingredient else 0
