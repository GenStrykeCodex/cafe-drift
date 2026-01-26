from utils.file_handler import load_json, save_json, load_with_integrity, save_with_integrity
from models.player import Player

PLAYER_FILE = "player_stats.json"


def show_main_menu():
    print("\n☕ Café Drift ☕")
    print("1. Start New Game")
    print("2. Continue")
    print("3. Reset Game")
    print("4. Exit")


def start_new_game():
    print("\nStarting a new game...")

    player = Player(
        name="Barista",
        stage=1,
        money=0,
        orders_completed=0,
        orders_failed=0,
        orders_rejected=0
    )

    save_with_integrity("player_stats.json", player.to_dict())
    print("New game initialized!")


def continue_game():
    print("\nLoading saved game...")

    data, is_valid = load_with_integrity("player_stats.json", default={})

    if not data:
        print("No saved game found.")
        return

    if not is_valid:
        print("⚠ Save file integrity check failed!")
        print("The save data may have been modified. DATA CORRUPTED!")
        print("Please reset the game to continue.")
        return

    player = Player.from_dict(data)
    print(f"Welcome back, {player.name}!")
    print(f"Stage: {player.stage} | Money: {player.money}")


def reset_game():
    confirm = input("\nAre you sure you want to reset the game? (y/n): ").lower()

    if confirm == "y":
        save_json("player_stats.json", {})
        save_json("inventory.json", {})
        save_json("integrity.json", {})
        print("Game data has been reset.")
    else:
        print("Reset cancelled.")


def main():
    while True:
        show_main_menu()
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            start_new_game()
        elif choice == "2":
            continue_game()
        elif choice == "3":
            reset_game()
        elif choice == "4":
            print("\nThanks for visiting Café Drift. See you next time ☕")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
