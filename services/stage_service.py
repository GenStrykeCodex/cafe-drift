from services.ingredient_service import get_unlocked_ingredients

STAGE_UNLOCK_REQUIREMENTS = {
    1: 5,
    2: 10,
    3: 15,
    4: 20,
}


def can_level_up(player) -> bool:
    required_orders = STAGE_UNLOCK_REQUIREMENTS.get(player.stage)
    if required_orders is None:
        return False  # Max stage reached

    return player.orders_completed >= required_orders


def level_up(player) -> list:
    if not can_level_up(player):
        return []

    old_stage = player.stage
    player.stage += 1

    # Keep skill_level aligned for now
    player.skill_level = player.stage

    # Determine newly unlocked ingredients
    before = get_unlocked_ingredients(old_stage)
    after = get_unlocked_ingredients(player.stage)

    before_keys = {i.key for i in before}
    newly_unlocked = [i for i in after if i.key not in before_keys]

    return newly_unlocked
