from utils.file_handler import (
    save_json,
    load_with_integrity,
    save_with_integrity,
)

from models.player import Player
from services.inventory_service import add_item
from services.ingredient_service import get_unlocked_ingredients
from ui.inventory_display import display_inventory

PLAYER_FILE = "player_stats.json"


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
    print("4. Exit to Main Menu")


# Persistence Actions

def start_new_game() -> Player:
    print("\nStarting a new game...")

    default_name = "Barista"
    name_input = input(f"Enter your name (press Enter to keep '{default_name}'): ").strip()

    if name_input:
        player_name = name_input
    else:
        player_name = default_name

    player = Player(
        name = player_name,
        stage = 1,
        money = 0,
        orders_completed = 0,
        orders_failed = 0,
        orders_rejected = 0,
    )

    save_with_integrity(PLAYER_FILE, player.to_dict())
    print(f"\nWelcome, {player.name}! Your café journey begins")

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
            add_item(player.inventory, keys[choice - 1], 1)
            print("Ingredient added to inventory ☕")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


# Game Loop

def run_game(player: Player):
    print(f"\nWelcome to Café Drift, {player.name} ☕")
    print("Your café is quiet… for now.\n")

    while True:
        show_game_menu()
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            display_inventory(player.inventory)

        elif choice == "2":
            restock_menu(player)

        elif choice == "3":
            unlocked = get_unlocked_ingredients(player.stage)
            print("\n🔓  Unlocked Ingredients")
            print("─" * 30)
            for data in unlocked.values():
                print(f"- {data['name']}")
            print("─" * 30)

        elif choice == "4":
            print("\nStepping away from the counter…")
            break

        else:
            print("Invalid option. Try again.")


# Application Entry Point

def main():
    while True:
        show_main_menu()
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            player = start_new_game()
            run_game(player)

        elif choice == "2":
            player = continue_game()
            if player:
                run_game(player)

        elif choice == "3":
            reset_game()

        elif choice == "4":
            print("\nThanks for visiting Café Drift. See you next time.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
