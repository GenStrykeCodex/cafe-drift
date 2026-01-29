from typing import Dict

INGREDIENTS = {
    "coffee_beans": {
        "name": "Coffee Beans",
        "unlock_stage": 1,
    },
    "milk": {
        "name": "Milk",
        "unlock_stage": 1,
    },
    "sugar": {
        "name": "Sugar",
        "unlock_stage": 1,
    },
    "tea_leaves": {
        "name": "Tea Leaves",
        "unlock_stage": 1,
    },
    "water": {
        "name": "Water",
        "unlock_stage": 1,
    },
    "ice": {
        "name": "Ice",
        "unlock_stage": 2,
    },
    "chocolate": {
        "name": "Chocolate",
        "unlock_stage": 3,
    },
    "caramel": {
        "name": "Caramel Syrup",
        "unlock_stage": 4,
    },
}


def get_unlocked_ingredients(stage: int) -> Dict[str, Dict]:
    return {
        key: data
        for key, data in INGREDIENTS.items()
        if stage >= data["unlock_stage"]
    }


def is_ingredient_unlocked(ingredient_key: str, stage: int) -> bool:
    ingredient = INGREDIENTS.get(ingredient_key)

    if ingredient is None:
        return False

    return stage >= ingredient["unlock_stage"]


def get_ingredient_name(ingredient_key: str) -> str:
    return INGREDIENTS.get(ingredient_key, {}).get("name", ingredient_key)


def get_unlock_stage(ingredient_key: str) -> int | None:
    ingredient = INGREDIENTS.get(ingredient_key)

    if ingredient is None:
        return None

    return ingredient["unlock_stage"]
