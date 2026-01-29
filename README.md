# ☕ Café Drift

**Café Drift** is a cozy, text-based café simulation game built with **Python**, focused on calm progression, clean architecture, and learning-by-building.

You run a small café, prepare orders, manage ingredients, earn money, and gradually unlock new stages as your café grows.

> The project is developed incrementally using versioned alpha releases, prioritizing strong foundations over rushed features.

---

## Current Status

- **Version:** v0.4.0-alpha
- **Stage:** Add Random Stage-based Orders & Gameplay
- **Gameplay Status:** Basic Gameplay Implemented

Café Drift now features a functional gameplay loop where players receive café orders, make decisions, and see their progress persist across sessions.

> ⚠️ This project is in **alpha**. Features are incomplete and subject to change.

---

## Features (as of v0.4.0-alpha)

### Player System

* Player identity with optional name selection (default: *Barista*)
* Stage-based progression system
* Persistent player statistics:

  * Orders completed
  * Orders failed
  * Orders rejected
  * Money (future use)

### Inventory System

* Ingredient inventory with add/remove/check logic
* Inventory persistence using `inventory.json`
* Stage-based ingredient unlocks
* Cozy CLI inventory display

### Order System (Alpha)

* Fixed pool of predefined café orders
* Orders unlock based on player stage
* Random order generation from unlocked orders
* Player can:
  * Accept an order
  * Reject an order

* Ingredient validation on accepted orders
* Orders are marked as:
  * Completed
  * Failed
  * Rejected

* Order outcomes update persistent player stats

### Persistence & Safety

* JSON-based storage for player stats and inventory
* Hash-based integrity checks to detect save tampering
* Reset / Start / Continue game flow
* Centralized default game state via `default_state.json`

---

## ▶ How To Run

### 1️. Clone the Repository

```bash
git clone <repository-url>
cd School-Management-System
````

---

### 2️. Run The Program

```bash
python main.py
```

or (PyCharm users):

```
Right Click → Run main.py
```

---

## Planned Features

* Ingredient consumption on successful orders
* Money rewards and spending system
* More complex order recipes
* Stage progression via completed orders
* GUI version (Tkinter / Pygame) in future major releases

---

## Tech Stack

- **Language:** Python 3
- **Storage:** JSON (local persistence)
- **Architecture:** Modular, service-based design
- **Environment:** Virtual Environment (venv)

---

## Reset Game

Café Drift includes a **Reset Game** mechanism designed for testing and development.  
This resets player stats, inventory, and regenerates integrity data to ensure a clean state.

---

## Notes

* This project is built as a **learning-focused portfolio project**
* Not intended for production or commercial use
* Feedback and architectural suggestions are welcome

---

## Author

Developed by **GenStryke Codex**

GitHub: https://github.com/GenStrykeCodex/

---

## License

This project is licensed under the **MIT Licens**e.

---

### Final note

Café Drift is now **playable**, but still growing.
Each version adds one calm, intentional step toward a complete café experience.

---
