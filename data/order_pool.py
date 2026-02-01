from models.order import Order

ORDER_POOL = [
    # ===== Stage 1 Orders =====
    Order(
        name="Tea",
        required_ingredients={
            "tea_leaves": 2,
            "water": 2,
            "milk": 1
        },
        min_stage=1
    ),
    Order(
        name="Coffee",
        required_ingredients={
            "coffee_beans": 2,
            "milk": 1
        },
        min_stage=1
    ),
    Order(
        name="Milkshake",
        required_ingredients={
            "milk": 3,
            "sugar": 2
        },
        min_stage=1
    ),
    Order(
        name="Black Coffee",
        required_ingredients={
            "coffee_beans": 1,
            "water": 2
        },
        min_stage=1
    ),
    Order(
        name="Sweet Tea",
        required_ingredients={
            "tea_leaves": 1,
            "water": 2,
            "sugar": 2
        },
        min_stage=1
    ),

    # ===== Stage 2 Orders =====
    Order(
        name="Iced Coffee",
        required_ingredients={
            "coffee_beans": 2,
            "milk": 1,
            "ice": 3
        },
        min_stage=2
    ),
    Order(
        name="Iced Tea",
        required_ingredients={
            "tea_leaves": 1,
            "water": 2,
            "ice": 2
        },
        min_stage=2
    ),
    Order(
        name="Vanilla Latte",
        required_ingredients={
            "coffee_beans": 2,
            "milk": 2,
            "vanilla_syrup": 1
        },
        min_stage=2
    ),
    Order(
        name="Chocolate Milk",
        required_ingredients={
            "milk": 2,
            "chocolate_syrup": 2,
            "sugar": 1
        },
        min_stage=2
    ),
    Order(
        name="Creamy Coffee",
        required_ingredients={
            "coffee_beans": 1,
            "cream": 2,
            "sugar": 1
        },
        min_stage=2
    ),

    # ===== Stage 3 Orders =====
    Order(
        name="Lemon Tea",
        required_ingredients={
            "tea_leaves": 2,
            "water": 2,
            "lemon": 2
        },
        min_stage=3
    ),
    Order(
        name="Honey Latte",
        required_ingredients={
            "coffee_beans": 2,
            "milk": 2,
            "honey": 2
        },
        min_stage=3
    ),
    Order(
        name="Hot Chocolate",
        required_ingredients={
            "milk": 3,
            "cocoa_powder": 2,
            "sugar": 2
        },
        min_stage=3
    ),
    Order(
        name="Caramel Macchiato",
        required_ingredients={
            "coffee_beans": 2,
            "milk": 2,
            "caramel_syrup": 2,
            "vanilla_syrup": 1
        },
        min_stage=3
    ),
    Order(
        name="Iced Mocha",
        required_ingredients={
            "coffee_beans": 2,
            "milk": 1,
            "chocolate_syrup": 2,
            "ice": 3
        },
        min_stage=3
    ),

    # ===== Stage 4 Orders =====
    Order(
        name="Chai Latte",
        required_ingredients={
            "tea_leaves": 2,
            "milk": 2,
            "cinnamon": 1,
            "honey": 1
        },
        min_stage=4
    ),
    Order(
        name="Espresso",
        required_ingredients={
            "espresso_shot": 2,
            "water": 1
        },
        min_stage=4
    ),
    Order(
        name="Cappuccino",
        required_ingredients={
            "espresso_shot": 2,
            "milk": 2,
            "whipped_cream": 2
        },
        min_stage=4
    ),
    Order(
        name="Butter Coffee",
        required_ingredients={
            "coffee_beans": 2,
            "butter": 2,
            "cream": 1
        },
        min_stage=4
    ),
    Order(
        name="Cinnamon Hot Chocolate",
        required_ingredients={
            "milk": 3,
            "cocoa_powder": 2,
            "cinnamon": 2,
            "whipped_cream": 2
        },
        min_stage=4
    ),

    # ===== Stage 5 Orders =====
    Order(
        name="Mint Mocha",
        required_ingredients={
            "espresso_shot": 2,
            "milk": 2,
            "chocolate_syrup": 2,
            "mint": 2
        },
        min_stage=5
    ),
    Order(
        name="Almond Milk Latte",
        required_ingredients={
            "espresso_shot": 2,
            "almond_milk": 3,
            "vanilla_syrup": 1
        },
        min_stage=5
    ),
    Order(
        name="Oat Milk Cappuccino",
        required_ingredients={
            "espresso_shot": 2,
            "oat_milk": 2,
            "cinnamon": 1,
            "whipped_cream": 2
        },
        min_stage=5
    ),
    Order(
        name="Spiced Latte",
        required_ingredients={
            "espresso_shot": 2,
            "milk": 2,
            "nutmeg": 1,
            "cinnamon": 2
        },
        min_stage=5
    ),
    Order(
        name="Peppermint Hot Chocolate",
        required_ingredients={
            "oat_milk": 3,
            "cocoa_powder": 3,
            "mint": 2,
            "whipped_cream": 2
        },
        min_stage=5
    ),
]