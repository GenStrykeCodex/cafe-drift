import random
from data.order_pool import ORDER_POOL
from models.order import Order


# Returns all orders available for the given player stage.
def get_unlocked_orders(player_stage: int) -> list:
    unlocked_orders = []

    for order in ORDER_POOL:
        if order.is_available(player_stage):
            unlocked_orders.append(order)

    return unlocked_orders


# Picks a random unlocked order for the player.
def generate_random_order(player_stage: int) -> Order | None:
    unlocked_orders = get_unlocked_orders(player_stage)

    if not unlocked_orders:
        return None

    return random.choice(unlocked_orders)