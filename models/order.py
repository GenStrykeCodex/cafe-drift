class Order:
    def __init__(
        self,
        name: str,
        required_ingredients: dict,
        min_stage: int,
    ):
        self.name = name
        self.required_ingredients = required_ingredients
        self.min_stage = min_stage
        self.status = "pending"  # pending | completed | failed | rejected

    def mark_completed(self):
        self.status = "completed"

    def mark_failed(self):
        self.status = "failed"

    def mark_rejected(self):
        self.status = "rejected"

    def is_available(self, player_stage: int) -> bool:
        return player_stage >= self.min_stage

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "required_ingredients": self.required_ingredients,
            "min_stage": self.min_stage,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict):
        order = cls(
            name=data["name"],
            required_ingredients=data["required_ingredients"],
            min_stage=data["min_stage"],
        )
        order.status = data.get("status", "pending")
        return order
