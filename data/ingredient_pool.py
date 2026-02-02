from models.ingredient import Ingredient

INGREDIENT_POOL = [
    # ---------- Stage 1 ----------
    Ingredient(
        key="water",
        name="Water",
        base_cost=5,
        unlock_stage=1,
        description="Fresh filtered water."
    ),
    Ingredient(
        key="sugar",
        name="Sugar",
        base_cost=10,
        unlock_stage=1,
        description="Sweetens the mood."
    ),
    Ingredient(
        key="tea_leaves",
        name="Tea Leaves",
        base_cost=15,
        unlock_stage=1,
        description="Aromatic tea leaves."
    ),
    Ingredient(
        key="coffee_beans",
        name="Coffee Beans",
        base_cost=20,
        unlock_stage=1,
        description="Rich roasted coffee beans."
    ),
    Ingredient(
        key="milk",
        name="Milk",
        base_cost=25,
        unlock_stage=1,
        description="Creamy fresh milk."
    ),

    # ---------- Stage 2 ----------
    Ingredient(
        key="ice",
        name="Ice",
        base_cost=5,
        unlock_stage=2,
        description="Perfect for chilled drinks."
    ),
    Ingredient(
        key="vanilla_syrup",
        name="Vanilla Syrup",
        base_cost=20,
        unlock_stage=2,
        description="Smooth vanilla sweetness."
    ),
    Ingredient(
        key="chocolate_syrup",
        name="Chocolate Syrup",
        base_cost=25,
        unlock_stage=2,
        description="Rich chocolate flavor."
    ),
    Ingredient(
        key="cream",
        name="Cream",
        base_cost=30,
        unlock_stage=2,
        description="Extra indulgence."
    ),

    # ---------- Stage 3 ----------
    Ingredient(
        key="lemon",
        name="Lemon",
        base_cost=15,
        unlock_stage=3,
        description="Fresh citrus kick."
    ),
    Ingredient(
        key="honey",
        name="Honey",
        base_cost=20,
        unlock_stage=3,
        description="Natural sweetness."
    ),
    Ingredient(
        key="cocoa_powder",
        name="Cocoa Powder",
        base_cost=25,
        unlock_stage=3,
        description="Deep chocolate notes."
    ),
    Ingredient(
        key="caramel_syrup",
        name="Caramel Syrup",
        base_cost=30,
        unlock_stage=3,
        description="Golden caramel sweetness."
    ),

    # ---------- Stage 4 ----------
    Ingredient(
        key="cinnamon",
        name="Cinnamon",
        base_cost=15,
        unlock_stage=4,
        description="Fresh cinnamon."
    ),
    Ingredient(
        key="butter",
        name="Butter",
        base_cost=25,
        unlock_stage=4,
        description="A block of salted butter."
    ),
    Ingredient(
        key="whipped_cream",
        name="Whipped Cream",
        base_cost=30,
        unlock_stage=4,
        description="A light and fluffy cream."
    ),
    Ingredient(
        key="espresso_shot",
        name="Espresso Shot",
        base_cost=40,
        unlock_stage=4,
        description="An explosion of intense coffee flavor."
    ),

    # ---------- Stage 5 ----------
    Ingredient(
        key="mint",
        name="Mint",
        base_cost=15,
        unlock_stage=5,
        description="Cool. Refreshing. A burst of fresh flavor."
    ),
    Ingredient(
        key="nutmeg",
        name="Nutmeg",
        base_cost=20,
        unlock_stage=5,
        description="A fragrant, warm, and sweet spice."
    ),
    Ingredient(
        key="almond_milk",
        name="Almond Milk",
        base_cost=35,
        unlock_stage=5,
        description="A light, dairy-free alternative with a subtle nutty flavor."
    ),
    Ingredient(
        key="oat_milk",
        name="Oat Milk",
        base_cost=35,
        unlock_stage=5,
        description="A creamy texture and mild oatmeal-like flavor."
    )
]
