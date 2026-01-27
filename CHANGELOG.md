# Café Drift

**Project Status** : `UNDER DEVELOPMENT` | **Gameplay Status** : `NOT IMPLEMENTED`

---

## v0.3.0-alpha Changelog — Inventory & Ingredient System

### Date : 27-01-2026

### Added

* Ingredient model with stage-based unlock design
* Inventory service with:
  * Add items
  * Remove items
  * Availability checks
* Ingredient unlock logic tied to player stage
* Cozy inventory display UI for CLI
* Player name selection on new game start (default: *Barista*)
* Integrated inventory, ingredient, and display systems into the game loop

### Improved

* Main game loop now feels interactive and “alive”
* Better separation of concerns between:

  * Models
  * Services
  * UI helpers
* Cleaner and more maintainable `main.py` structure

### Notes

* No order system yet (planned for next alpha)
* Inventory is currently restock-only (no consumption)
* This version focuses on **foundation gameplay systems**

---

## v0.2.0-alpha Changelog – CLI Menu & Save Integrity

### Date : 26-01-2026

### Added
- Basic CLI main menu with options:
  - Start New Game
  - Continue Game
  - Reset Game
  - Exit
- Persistent player data loading on program start.
- JSON-based save system for player stats and inventory.
- Save file integrity check using hash validation to detect tampering.
- Separate integrity data storage for runtime validation.
- Reset Game functionality with confirmation prompt to clear all saved data.

### Changed
- Player progression simplified by treating **stage and level as a single variable**.
- Centralized file handling logic via `utils/file_handler.py`.
- Improved fault tolerance when loading missing or corrupted save files.

### Fixed
- Prevented crashes caused by missing or malformed save data.
- Ensured safe fallback to default values during first launch or failed integrity checks.

### Notes
- This is an **early alpha release**.
- Gameplay mechanics are not yet implemented.
- Current focus is on architecture, persistence, and system stability.

---

## v0.1.0-alpha Changelog — Project Initialization

### Date : 25-01-2026

### Added
- Initial project structure
- Modular folder layout (models, services, utils, data)
- Entry point (`main.py`)
- Configuration file (`config.py`)
- JSON-based persistence design
- Default game state definition
- Placeholder files for future development
- Virtual environment support
- Reset Game system design (foundation)

### Notes
- No gameplay logic implemented yet
- This version focuses purely on architecture and planning
- Intended as a stable foundation for future versions

---

☕ *The café doors are not open yet, but the lights are on.*

---