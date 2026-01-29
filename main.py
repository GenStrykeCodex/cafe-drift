from utils.file_handler import (
    load_json,
    save_json,
    load_with_integrity,
    save_with_integrity,
)

from models.player import Player
from services.inventory_service import add_item, has_required_ingredients
from services.ingredient_service import get_unlocked_ingredients
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


# Persistence Actions

def start_new_game() -> Player:
    print("\nStarting a new game...\n")

    # Load default state
    default_state = load_json("default_state.json", default={})

    default_player = default_state.get("player_stats", {})
    default_inventory = default_state.get("inventory", {})

    # Name selection
    default_name = default_player.get("name", "Barista")
    name_input = input(
        f"Enter your name (press Enter to keep '{default_name}'): "
    ).strip()

    player_name = name_input if name_input else default_name

    # Create player using defaults (except name)
    player = Player(
        name=player_name,
        stage=default_player.get("stage", 1),
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
    unlocked = get_unlocked_ingredients(player.stage)

    if not unlocked:
        print("No ingredients unlocked yet.")
        return

    print("\n🛒  Restock Ingredients")
    print("─" * 30)

    keys = list(unlocked.keys())
    for i, key in enumerate(keys, start=1):
        print(f"{i}. {unlocked[key]['name']}")

    try:
        choice = int(input("\nChoose ingredient number: "))
        if 1 <= choice <= len(keys):
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                add_item(player.inventory, keys[choice - 1], quantity)
                print("Ingredient added to inventory ☕")
            else:
                print("Ingredient quantity must be greater than 0.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

    save_with_integrity(INVENTORY_FILE, player.inventory)


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

    choice = input("Accept order? (y = accept / n = reject): ").lower()

    if choice == "n":
        order.mark_rejected()
        player.orders_rejected += 1
        print("Order rejected politely ☁️")
        return

    if choice != "y":
        print("Invalid choice. Order ignored.")
        return

    # Accepted → validate ingredients
    if has_required_ingredients(player.inventory, order.required_ingredients):
        order.mark_completed()
        player.orders_completed += 1
        print("Order completed successfully ☕✨")
    else:
        order.mark_failed()
        player.orders_failed += 1
        print("Not enough ingredients — order failed 💭")

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
                for data in unlocked.values():
                    print(f"- {data['name']}")
                print("─" * 30)
                break

            elif choice == "4":
                handle_order(player)
                break

            elif choice == "5":
                print("\nStepping away from the counter…")
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
