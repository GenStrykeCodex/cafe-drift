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

from services.stage_service import level_up
from models.player import Player
from services.inventory_service import add_item, has_required_ingredients, remove_ingredients
from services.ingredient_service import get_unlocked_ingredients, get_ingredient_name
from ui.inventory_display import display_inventory
from services.order_service import generate_random_order

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
    print("5. Close the Café")

# UI Helper

def show_end_of_day_recap(player) -> None:
    print("\n" + "=" * 45)
    print("End of Day Summary")
    print("=" * 45)

    print(f"Barista: {player.name}")
    print(f"Stage: {player.stage}")
    print("-" * 45)

    print(f"✅ Orders Completed : {player.orders_completed}")
    print(f"❌ Orders Failed    : {player.orders_failed}")
    print(f"🚫 Orders Rejected  : {player.orders_rejected}")

    print("-" * 45)
    print(f"💰 Current Balance  : {player.money} coins")

    print("=" * 45)

    if player.orders_completed > player.orders_failed:
        print("\nA productive day! Your café is growing.")
    elif player.orders_failed > 0:
        print("\nA learning day — tomorrow will be better.")
    else:
        print("\nA calm and quiet day.")

    print("=" * 45 + "\n")


# Persistence Actions

def start_new_game() -> Player:
    print("\nStarting a new game...\n")

    # Load default state
    default_state = load_json("default_state.json", default={})

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
        orders_completed=default_player.get("orders_completed", 0),
        orders_failed=default_player.get("orders_failed", 0),
        orders_rejected=default_player.get("orders_rejected", 0),
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
    print("─" * 30)

    order_run = True

    while order_run:
        choice = input("Accept order? (y = accept / n = reject): ").lower()

        if choice == "n":
            order.mark_rejected()
            player.orders_rejected += 1
            print("\n🚫 Order rejected. No money gained or lost.")
            return

        elif choice == "y":
            # Accepted → validate ingredients
            if has_required_ingredients(player.inventory, order.required_ingredients):
                price = calculate_order_price(order.required_ingredients, player.stage)

                # Deduct ingredients
                remove_ingredients(player.inventory, order.required_ingredients)

                # Add money
                player.money += price
                player.orders_completed += 1

                order.mark_completed()

                print("Order completed successfully ☕✨")
                print(f"You earned +{price} coins 💰")

                # Stage progression check
                newly_unlocked = level_up(player)

                if newly_unlocked:
                    print("\n✨ Stage Up!")
                    print(f"Your café has reached Stage {player.stage} ☕")

                    print("\n🔓 New ingredients unlocked:")
                    for ingredient in newly_unlocked:
                        print(f"• {ingredient.name}")

                order_run = False

            else:
                price = calculate_order_price(order.required_ingredients, player.stage)
                penalty = calculate_failure_penalty(price)

                # Deduct money
                player.money -= penalty
                player.orders_failed += 1

                order.mark_failed()

                print(f"\n❌ Order failed!")
                print(f"You lost {penalty} coins 💸")

                order_run = False

    save_with_integrity(PLAYER_FILE, player.to_dict())
    save_with_integrity(INVENTORY_FILE, player.inventory)


# Game Loop

def run_game(player: Player):
    print(f"\nWelcome to Café Drift, {player.name} ☕")
    print("Your café is quiet… for now.\n")

    while True:
        show_game_menu()

        while True:
            choice = input("\nSelect an option: ").strip()

            if choice == "1":
                display_inventory(player.inventory)
                break

            elif choice == "2":
                restock_menu(player)
                break

            elif choice == "3":
                unlocked = get_unlocked_ingredients(player.stage)
                print("\n🔓  Unlocked Ingredients")
                print("─" * 30)

                for ingredient in unlocked:
                    print(f"- {ingredient.name}")

                print("─" * 30)
                break

            elif choice == "4":
                handle_order(player)
                break

            elif choice == "5":
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
