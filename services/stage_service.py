from services.ingredient_service import get_unlocked_ingredients
from utils.file_handler import load_json


STAGE_FILE = "stage_rules.json"
STORAGE_FILE = "capacity_upgrades.json"


# Check level up eligibility
def can_level_up(player) -> bool:
    stage_rules = load_json(STAGE_FILE, default={}, data_dir="data")

    next_stage = str(player.stage + 1)

    if next_stage not in stage_rules:
        return False

    rules = stage_rules[next_stage]

    return (
        player.orders_completed >= rules["min_orders_completed"]
        and player.total_money_earned >= rules["min_total_money_earned"]
    )


# Level up player if conditions fulfilled
def level_up(player):
    if player.has_leveled_up_today:
        return [], 0

    if not can_level_up(player):
        return [], 0

    player.stage += 1

    upgrades = load_json(STORAGE_FILE, default={}, data_dir="data")
    capacity_increase = upgrades[str(player.stage)]

    player.storage_capacity += capacity_increase

    player.has_leveled_up_today = True

    unlocked_ingredients = []
    for ingredient in get_unlocked_ingredients(player.stage):
        if ingredient.unlock_stage == player.stage:
            unlocked_ingredients.append(ingredient)

    return unlocked_ingredients, capacity_increase


# Get progress for next stage
def get_next_stage_progress(player) -> dict | None:
    stage_rules = load_json(STAGE_FILE, default={}, data_dir="data")

    next_stage = str(player.stage + 1)

    # If no further stages exist
    if next_stage not in stage_rules:
        return None

    rules = stage_rules[next_stage]

    return {
        "orders_completed": player.orders_completed,
        "required_orders": rules["min_orders_completed"],
        "money_earned": player.total_money_earned,
        "required_money": rules["min_total_money_earned"],
    }
