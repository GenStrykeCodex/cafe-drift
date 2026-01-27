class Ingredient:
    def __init__(
        self,
        key: str,
        name: str,
        base_cost: int,
        unlock_stage: int,
        description: str = ""
    ):
        self.key = key
        self.name = name
        self.base_cost = base_cost
        self.unlock_stage = unlock_stage
        self.description = description
