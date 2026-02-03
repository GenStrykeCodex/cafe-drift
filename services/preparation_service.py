import random

MIN_SUCCESS_RATE = 60
MAX_SUCCESS_RATE = 95
BASE_SUCCESS_RATE = 80

# Calculate preparation success chance
def calculate_success_rate(skill_level: int, ingredient_count: int) -> int:
    complexity_penalty = max(ingredient_count - 1, 0) * 5
    skill_bonus = skill_level * 3

    success_rate = BASE_SUCCESS_RATE + skill_bonus - complexity_penalty
    return max(MIN_SUCCESS_RATE, min(MAX_SUCCESS_RATE, success_rate))


def attempt_preparation(player, order) -> tuple[bool, int]:
    ingredient_count = len(order.required_ingredients)

    skill_level = player.skill_level
    ingredient_count = ingredient_count

    success_rate = calculate_success_rate(skill_level,ingredient_count)

    roll = random.randint(1, 100)
    return roll <= success_rate, success_rate
