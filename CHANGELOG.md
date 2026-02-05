# Café Drift

**Project Status** : `UNDER DEVELOPMENT` | **Gameplay Status** : `CORE GAMEPLAY`

---

## v0.8.0-alpha Changelog — Progression & Storage Overhaul

### Date : 05-02-2026

### Added

- Data-driven stage progression using `stage_rules.json`
- `total_money_earned` stat to fairly gate progression
- Player storage capacity as a persistent stat
- Stage-based storage capacity upgrades via `capacity_upgrades.json`
- Café status display showing:
  - Stage
  - Inventory usage
  - Storage capacity
  - Progress toward next stage
- Player feedback when:
  - Stage progression is locked
  - Inventory capacity is full
- Clear end-of-day progression summary

### Changed

- Separated configuration data from runtime save data
- Refactored JSON load/save utilities to support configurable data directories
- Stage level-up logic refactored to be rule-based and incremental
- Inventory restocking now respects storage capacity limits
- End-of-day recap updated to reflect progression systems

### Improved

- Cleaner separation of UI, services, and game logic
- Safer progression flow (prevents accidental multi-stage jumps)
- Improved player guidance for restocking and progression
- Player Guide updated to reflect new mechanics

### Notes

- Save file structure changed in this version
- Older saves may not be compatible
- Café Drift remains in active alpha development

---

## v0.7.0-alpha Changelog — Preparation & Player Guidance

### Date : 03-02-2026

### Added
- Preparation success logic with success rate
- Imperfect order handling with reduced rewards
- Player Guide system with multiple guide files
- FAQ for common player questions
- Clear separation between failed and imperfect orders
- Improved order handling flow

### Improved
- Cozy, forgiving gameplay balance
- Player feedback during order preparation
- Clarity around stats, inventory, and progression
- Documentation for new players

---

## v0.6.0-alpha Changelog – Stage Progression & Unified Ingredient System

### Date : 02-02-2026

### Added
- Stage progression system based on completed orders
- Automatic stage-up after meeting progression requirements
- New ingredients unlocked on stage advancement
- Skill level introduced (mirrors stage for now)
- Centralized Ingredient Pool using Ingredient model
- Stage-based unlock feedback for players

### Changed
- Ingredient data refactored into a single source of truth
- Economy service now derives prices from Ingredient objects
- Main gameplay flow updated to support stage progression
- Ingredient costs and unlock stages fully data-driven

### Removed
- Deprecated hardcoded ingredient definitions
- Deprecated separate ingredient cost mapping

### Notes
- Gameplay now provides a clear sense of advancement
- Project remains in **alpha** as core systems continue to evolve

---

## v0.5.0-alpha Changelog – Core Economy & Gameplay Loop

### Date : 01-02-2026

### Added
- Ingredient-based economy system
- Formula-driven order pricing
- Stage-based price multipliers
- Money rewards for completed orders
- 10% penalty for failed orders
- Inventory consumption on successful orders
- Bulk ingredient purchasing with cost validation
- End-of-day earnings recap
- Cozy feedback messages for earnings and failures

### Changed
- Order prices are no longer hardcoded
- Inventory.json is now fully integrated into gameplay
- Order pool moved to `data/order_pool.py` for scalability
- Improved CLI formatting for restock menu

### Fixed
- Player stats not updating after order completion
- Inventory not persisting correctly after gameplay actions

### Notes
- Gameplay status upgraded from **Basic Gameplay** to **Core Gameplay (Alpha)**
- Focus remains on correctness, balance, and clean architecture

---

## v0.4.0-alpha Changelog — Orders & Default State System

### Date : 29-01-2026

### Added

* Order system foundation:

  * Fixed order pool with stage-based availability
  * Random order generation from unlocked orders
* Order interaction flow:

  * Player can accept or reject orders
  * Ingredient validation on accepted orders
* Order outcome tracking:

  * Completed orders
  * Failed orders
  * Rejected orders
* Default game state support via `default_state.json`:

  * Default player stats
  * Default inventory
  * Player name overridden at game start
* Inventory persistence:

  * Inventory now properly loads and saves using `inventory.json`

### Improved

* Clear separation between:

  * Order data (model)
  * Order logic (service)
  * Game flow (main loop)
* Reduced hardcoded values by centralizing defaults in JSON
* More realistic and scalable game initialization flow

### Notes

* Orders do not consume ingredients yet
* No money rewards or preparation steps implemented
* This version focuses on **core gameplay flow**, not balance or realism

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