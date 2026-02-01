from typing import Dict


def add_item(inventory: Dict[str, int], ingredient_key: str, quantity: int = 1) -> None:
    if quantity <= 0:
        return

    inventory[ingredient_key] = inventory.get(ingredient_key, 0) + quantity


def remove_item(inventory: Dict[str, int], ingredient_key: str, quantity: int = 1) -> bool:
    if ingredient_key not in inventory or inventory[ingredient_key] < quantity:
        return False

    inventory[ingredient_key] -= quantity

    if inventory[ingredient_key] == 0:
        del inventory[ingredient_key]

    return True


def has_item(inventory: Dict[str, int], ingredient_key: str, quantity: int = 1) -> bool:
    return inventory.get(ingredient_key, 0) >= quantity


# Checks if the player has ingredients required for accepted order.
def has_required_ingredients(inventory: dict, required: dict) -> bool:
    for ingredient, qty_needed in required.items():
        if inventory.get(ingredient, 0) < qty_needed:
            return False
    return True


# Removes used ingredients from inventory after a successful order.
def remove_ingredients(inventory: dict, required_ingredients: dict) -> None:
    for ingredient, quantity in required_ingredients.items():
        remove_item(inventory, ingredient, quantity)
