from utils.file_handler import (
    load_json,
    save_json,
    load_with_integrity,
    save_with_integrity,
)

from services.economy_service import (
    calculate_order_price,
    calculate_failure_penalty
)

from services.inventory_service import (
    add_item,
    has_required_ingredients,
    get_inventory_count,
    remove_ingredients
)

from services.ingredient_service import (
    get_unlocked_ingredients,
    get_ingredient_name
)

from ui.status_display import (
    display_status,
    display_stage_progress,
    display_inventory_status
)

from models.player import Player
from services.stage_service import level_up
from services.preparation_service import attempt_preparation
from services.order_service import generate_random_order
from ui.inventory_display import display_inventory


PLAYER_FILE = "player_stats.json"
INVENTORY_FILE = "inventory.json"


# Menu Displays

def show_main_menu():
    print("\n ☕ Café Drift ☕")
    print("1. Start New Game")
    print("2. Continue")
    print("3. Reset Game")
    print("4. Exit")


def show_game_menu():
    print("\n ☕ Inside the Café")
    print("1. View Inventory")
    print("2. Restock Ingredient")
    print("3. View Unlocked Ingredients")
    print("4. Take Order")
    print("5. View Café Status")
    print("6. Close the Café")


# UI Helper

def show_end_of_day_recap(player) -> None:
    print("\n" + "=" * 50)
    print("☾ End of Day Summary")
    print("=" * 50)

    print(f"Barista: {player.name}")
    print(f"Stage  : {player.stage}")
    print("-" * 50)

    print(f"✅ Orders Completed : {player.orders_completed}")
    print(f"❌ Orders Failed    : {player.orders_failed}")
    print(f"🚫 Orders Rejected  : {player.orders_rejected}")

    print("-" * 50)
    print(f"💰 Current Balance     : {player.money} coins")
    print(f"📈 Total Money Earned  : {player.total_money_earned} coins")

    print("-" * 50)
    print()

    # Stage progression feedback
    display_stage_progress(player)

    print()
    print("=" * 50)

    # Cozy day summary
    if player.orders_completed > player.orders_failed:
        print("☕ A productive day! Your café is steadily growing.")
    elif player.orders_failed > 0:
        print("🌱 A learning day — tomorrow will be better.")
    else:
        print("🌙 A calm and quiet day.")

    print("=" * 50 + "\n")

    # Reset daily progression lock
    player.has_leveled_up_today = False

    save_with_integrity(PLAYER_FILE, player.to_dict())
    save_with_integrity(INVENTORY_FILE, player.inventory)


# Persistence Actions

def start_new_game() -> Player:
    print("\nStarting a new game...\n")

    # Load default state
    default_state = load_json("default_state.json", default={}, data_dir="data")

    default_player = default_state.get("player_stats", {})
    default_inventory = default_state.get("inventory", {})

    # Name selection
    default_name = default_player.get("name", "Barista")
    name_input = input(f"Enter your name (press Enter to keep '{default_name}'): ").strip()

    player_name = name_input if name_input else default_name

    # Create player using defaults (except name)
    player = Player(
        name=player_name,
        stage=default_player.get("stage", 1),
        skill_level=default_player.get("skill_level", 1),
        money=default_player.get("money", 0),
        total_money_earned=default_player.get("total_money_earned", 0),
        has_leveled_up_today=default_player.get("has_leveled_up_today", False),
        orders_completed=default_player.get("orders_completed", 0),
        orders_failed=default_player.get("orders_failed", 0),
        orders_rejected=default_player.get("orders_rejected", 0),
        storage_capacity=default_player.get("storage_capacity", 30),
    )

    player.inventory = default_inventory.copy()

    save_with_integrity(PLAYER_FILE, player.to_dict())
    save_with_integrity(INVENTORY_FILE, player.inventory)

    print(f"\nWelcome, {player.name}! Your café journey begins ☕")
    return player


def continue_game() -> Player | None:
    print("\nLoading saved game...")

    data, is_valid = load_with_integrity(PLAYER_FILE, default={})

    if not data:
        print("No saved game found.")
        return None

    if not is_valid:
        print("⚠ Save file integrity check failed!")
        print("Save data may have been modified.")
        print("Please reset the game to continue.")
        return None

    player = Player.from_dict(data)

    inventory_data, inventory_ok = load_with_integrity(
        INVENTORY_FILE, default={}
    )

    if not inventory_ok:
        print("⚠ Inventory file integrity check failed.")
        print("Reset the game to continue safely.")
        return None

    player.inventory = inventory_data

    print(f"Welcome back, {player.name}!")
    print(f"Stage: {player.stage} | Money: {player.money}")

    return player


def reset_game():
    confirm = input("\nAre you sure you want to reset the game? (y/n): ").lower()

    if confirm == "y":
        save_json("player_stats.json", {})
        save_json("inventory.json", {})
        save_json("integrity.json", {})
        print("Game data has been reset.")
    else:
        print("Reset cancelled.")


# Gameplay Actions

def restock_menu(player: Player):
    unlocked_ingredients = get_unlocked_ingredients(player.stage)

    if not unlocked_ingredients:
        print("No ingredients unlocked yet.")
        return

    print("\n🛒  Restock Ingredients")
    print("─" * 40)

    for i, ingredient in enumerate(unlocked_ingredients, start=1):
        print(f"{i}. {ingredient.name:<18} — {ingredient.base_cost:>3} coins each")

    print("─" * 40)
    display_inventory_status(player)
    print("─" * 40)

    try:
        choice = int(input("\nChoose ingredient number: "))
        if not (1 <= choice <= len(unlocked_ingredients)):
            print("Invalid choice.")
            return

        ingredient = unlocked_ingredients[choice - 1]

        quantity = int(input("Enter quantity to buy: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        inventory_count = get_inventory_count(player.inventory)

        if inventory_count + quantity > player.storage_capacity:
            print("\nNot enough storage capacity.")
            print("Continue preparing orders to make space.")
            return

        total_cost = ingredient.base_cost * quantity

        print(f"\n🧾 {ingredient.name} x{quantity}")
        print(f"Total cost: {total_cost} coins")

        if player.money < total_cost:
            print("❌ Not enough money to complete this purchase.")
            print(f"Your balance: {player.money} coins")
            return

        # Deduct money
        player.money -= total_cost

        # Add to inventory
        add_item(player.inventory, ingredient.key, quantity)

        print(f"✅ Purchased {quantity} {get_ingredient_name(ingredient.key)}(s)!")
        print(f"Remaining balance: {player.money} coins 💰")

        print("─" * 40)
        display_inventory_status(player)
        print("─" * 40)

        if inventory_count + quantity == player.storage_capacity:
            print("\nInventory is FULL.")
            print("No more space.")

        save_with_integrity(PLAYER_FILE, player.to_dict())
        save_with_integrity(INVENTORY_FILE, player.inventory)

    except ValueError:
        print("Please enter valid numbers only.")


def handle_order(player: Player):
    order = generate_random_order(player.stage)

    if not order:
        print("\nNo orders available at your current stage.")
        return

    print("\n📋 New Order")
    print("─" * 30)
    print(f"Order: {order.name}")
    print("Ingredients required:")
    for ingredient, qty in order.required_ingredients.items():
        print(f"  - {ingredient} x{qty}")
    print(f"Base Price: {calculate_order_price(order.required_ingredients, player.stage)} coins")
    print("─" * 30)

    order_run = True

    while order_run:
        choice = input("Accept order? (y = accept / n = reject): ").lower()

        if choice == "n":
            player.orders_rejected += 1
            print("\n🚫 Order rejected. No money gained or lost.")

            order_run = False

        elif choice == "y":
            handle_order_preparation(player, player.inventory, order)

            # Stage progression check
            newly_unlocked, capacity_increase = level_up(player)

            if newly_unlocked:
                print("\n✨ Stage Up!")
                print(f"Your café has reached Stage {player.stage} ☕")

                print(f"\nStorage capacity +{capacity_increase}")

                print("\n🔓 New ingredients unlocked:")
                for ingredient in newly_unlocked:
                    print(f"• {ingredient.name}")

            order_run = False

        else:
            print("Invalid choice.")

    save_with_integrity(PLAYER_FILE, player.to_dict())
    save_with_integrity(INVENTORY_FILE, player.inventory)


def handle_order_preparation(player, inventory: dict, order) -> None:
    base_price = calculate_order_price(order.required_ingredients, player.stage)

    # Validating ingredients
    if not has_required_ingredients(inventory, order.required_ingredients):
        penalty = calculate_failure_penalty(base_price)

        # Deduct money
        player.money -= penalty
        player.orders_failed += 1

        print(f"\n❌ Order failed!")
        print("You don't have enough ingredients!")
        print("💡 Hint: Always check and restock ingredients before taking orders.")
        print(f"You lost {penalty} coins 💸")
        return

    # Player has the ingredients
    success, success_rate = attempt_preparation(player, order)

    print(f"\n☕ Preparing... (Success chance: {success_rate}%)\n")

    # Deduct ingredients
    remove_ingredients(player.inventory, order.required_ingredients)

    if success:
        # Perfectly prepared order
        player.money += base_price
        player.total_money_earned += base_price

        print("✅ Order completed!")
        print("😆 The customer seems fully satisfied ☕✨")
        print(f"You earned +{base_price} coins 💰")

    else:
        # Imperfectly prepared order
        reduced_price = int(base_price * 0.9)
        player.money += reduced_price
        player.total_money_earned += reduced_price

        print("☑️ Order completed!")
        print("😐 The customer doesn't seem fully satisfied ☕")
        print("💡 Hint: Work on your skills to improve preparation quality.")
        print(f"You earned +{reduced_price} coins 💰 (10% Reduced)")

    player.orders_completed += 1

    save_with_integrity(PLAYER_FILE, player.to_dict())
    save_with_integrity(INVENTORY_FILE, player.inventory)
    return


# Game Loop

def run_game(player: Player):
    print(f"\nWelcome to Café Drift, {player.name} ☕")

    while True:
        show_game_menu()

        while True:
            choice = input("\nSelect an option: ").strip()

            if choice == "1":
                display_inventory(player.inventory)
                display_inventory_status(player)
                print("─" * 30)
                break

            elif choice == "2":
                restock_menu(player)
                break

            elif choice == "3":
                unlocked = get_unlocked_ingredients(player.stage)
                print("\n🔓 Unlocked Ingredients")
                print("─" * 30)

                for ingredient in unlocked:
                    print(f"- {ingredient.name}")

                print("─" * 30)
                break

            elif choice == "4":
                handle_order(player)
                break

            elif choice == "5":
                display_status(player)
                break

            elif choice == "6":
                print("\nStepping away from the counter…")
                show_end_of_day_recap(player)
                return

            else:
                print("Invalid option. Try again.")


# Application Entry Point

def main():
    while True:
        show_main_menu()

        while True:
            choice = input("\nSelect an option (1-4): ").strip()

            if choice == "1":
                player = start_new_game()
                run_game(player)
                break

            elif choice == "2":
                player = continue_game()
                if player:
                    run_game(player)
                break

            elif choice == "3":
                reset_game()
                break

            elif choice == "4":
                print("\nThanks for visiting Café Drift. See you next time.")
                return

            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
