# ☕ Café Drift

**Café Drift** is a cozy, text-based café simulation game built with **Python**, focused on calm progression, clean architecture, and learning-by-building.

You run a small café, prepare orders, manage ingredients, earn money, and gradually unlock new stages as your café grows.

> The project is developed incrementally using versioned alpha releases, prioritizing strong foundations over rushed features.

---

## Current Status

**Version:** v0.5.0-alpha  
**Gameplay State:** Core Gameplay Implemented (Alpha)

The game is playable in CLI and supports a full order → inventory → economy loop.

---

## Gameplay Overview

- Start a new café or continue from a saved state
- Orders appear based on player stage
- Players can:
  - Accept orders
  - Reject orders
- Accepted orders:
  - Validate ingredient availability
  - Consume ingredients on success
  - Earn money based on ingredient cost and stage
- Failed orders:
  - Apply a small money penalty (10%)
- Inventory is persistent and stage-gated
- Ingredients can be restocked using earned money
- End-of-day recap shows performance and balance

---

## Core Systems Implemented

### ✔ Player System
- Name (default: Barista, customizable)
- Stage-based progression
- Persistent stats (JSON + integrity check)

### ✔ Inventory System
- Add, remove, and batch-consume ingredients
- Inventory persistence
- Cozy CLI inventory display

### ✔ Order System
- Fixed, stage-based order pool
- Random order generation
- Accept / Reject flow
- Tracking of completed, failed, and rejected orders

### ✔ Economy System
- Ingredient-based pricing
- Formula-driven order value:
```
Order Price = Total Ingredient Cost × 1.5 × Stage Multiplier
```
- Prices rounded to nearest multiple of 5
- 10% penalty for failed orders
- Money persistence

### ✔ End-of-Day Recap
- Orders summary
- Current balance
- Cozy feedback messages

---

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

## Project Structure

```
cafe-drift/
│
├── data/
│   ├── ingredient_costs.py
│   ├── default_state.json
│   ├── integrity.json
│   ├── inventory.json
│   ├── player_stats.json
│   └── order_pool.py
│
├── models/
│   ├── player.py
│   ├── order.py
│   └── ingredient.py
│
├── services/
│   ├── inventory_service.py
│   ├── ingredient_service.py
│   ├── order_service.py
│   └── economy_service.py
│
├── utils/
│   ├── file_handler.py
│   └── validators.py
│
├── ui/
│   └── inventory_display.py
│
├── main.py
├── README.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## Roadmap (Upcoming)

- Preparation success chance
- Ingredient shop improvements
- Daily progression system
- Customer satisfaction / ratings
- GUI version (Tkinter / Pygame) in future releases

---

## ⚠ Disclaimer

This project is currently in **alpha**.  
Features and mechanics are still evolving, and breaking changes may occur.

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
