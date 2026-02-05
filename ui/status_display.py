from services.inventory_service import get_inventory_count
from services.stage_service import get_next_stage_progress


# Show Cafe Status
def display_status(player):
    print("\n📊 Café Status")
    print("-"*50)
    print(f"Player: {player.name}"+ " " * 20 + f"Balance: {player.money}")
    print(f"Stage: {player.stage}")
    print("-"*50)

    display_inventory_status(player)
    print("-"*50)

    display_stage_progress(player)
    print("-"*50)


# Show Storage Status
def display_inventory_status(player):
    inventory_count = get_inventory_count(player.inventory)
    inventory_capacity = player.storage_capacity

    print(f"Inventory status: {inventory_count} / {inventory_capacity}")


# Stage progression feedback
def display_stage_progress(player):
    progress = get_next_stage_progress(player)

    if progress:
        print(f"Progress towards Stage {player.stage + 1} -")
        print(f"• Orders completed: {progress['orders_completed']} / {progress['required_orders']}")
        print(f"• Money earned : {progress['money_earned']} / {progress['required_money']}")
    else:
        print("🏆 Maximum stage reached!")
