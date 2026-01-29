import random
from models.order import Order


ORDER_POOL = [
    # Stage 1 orders
    Order(
        name="Tea",
        required_ingredients={
            "tea_leaves": 1,
            "water": 1,
            "milk": 1
        },
        min_stage=1
    ),
    Order(
        name="Coffee",
        required_ingredients={
            "coffee_beans": 1,
            "milk": 1
        },
        min_stage=1
    ),
    Order(
        name="Milkshake",
        required_ingredients={
            "milk": 2,
            "sugar": 1
        },
        min_stage=1
    ),

    # Stage 2 orders (example)
    Order(
        name="Iced Coffee",
        required_ingredients={
            "coffee_beans": 1,
            "milk": 1,
            "ice": 1
        },
        min_stage=2
    ),
]


def get_unlocked_orders(player_stage: int) -> list:
    unlocked_orders = []
    for order in ORDER_POOL:
        if order.is_available(player_stage):
            unlocked_orders.append(order)

    return unlocked_orders


def generate_random_order(player_stage: int) -> Order | None:
    unlocked_orders = get_unlocked_orders(player_stage)

    if not unlocked_orders:
        return None

    return random.choice(unlocked_orders)
