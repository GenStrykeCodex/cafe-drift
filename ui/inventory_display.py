from typing import Dict
from services.ingredient_service import get_ingredient_name


def display_inventory(inventory: Dict[str, int]) -> None:
    print("\n📦 Your Inventory")
    print("─" * 30)

    if not inventory:
        print("Your shelves are empty ☁️")
        print("─" * 30)
        return

    for ingredient_key, quantity in inventory.items():
        name = get_ingredient_name(ingredient_key)
        print(f"{name:<20} x{quantity}")

    print("─" * 30)
