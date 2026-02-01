from data.ingredient_costs import INGREDIENT_COSTS

# Base multiplier applied to every order
BASE_MULTIPLIER = 1.5

# Stage-based price multipliers
STAGE_MULTIPLIERS = {
    1: 1.0,
    2: 1.25,
    3: 1.5,
    4: 1.75,
    5: 2.0,
}

# Penalty for failed orders (10%)
FAILURE_PENALTY_RATE = 0.10


# Calculates total cost of ingredients used in an order.
def calculate_ingredient_cost(ingredients: dict) -> int:
    total_cost = 0

    for ingredient, quantity in ingredients.items():
        cost = INGREDIENT_COSTS.get(ingredient, 0)
        total_cost += cost * quantity

    return total_cost


# Calculates final selling price of an order
def calculate_order_price(ingredients: dict, stage: int) -> int:

    ingredient_cost = calculate_ingredient_cost(ingredients)

    stage_multiplier = STAGE_MULTIPLIERS.get(stage, 1.0)
    raw_price = ingredient_cost * BASE_MULTIPLIER * stage_multiplier

    return round_to_nearest_5(raw_price)


# Calculates money deducted for a failed order
def calculate_failure_penalty(order_price: int) -> int:

    penalty = order_price * FAILURE_PENALTY_RATE
    return round_to_nearest_5(penalty)


def round_to_nearest_5(value: float) -> int:
    return int(round(value / 5) * 5)
