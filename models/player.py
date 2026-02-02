class Player:
    def __init__(
        self,
        name: str,
        stage: int,
        skill_level: int,
        money: int,
        orders_completed: int,
        orders_failed: int,
        orders_rejected: int,
        inventory: dict | None = None
    ):
        self.name = name
        self.stage = stage
        self.skill_level = skill_level
        self.money = money
        self.orders_completed = orders_completed
        self.orders_failed = orders_failed
        self.orders_rejected = orders_rejected
        self.inventory = inventory if inventory is not None else {}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", "Barista"),
            stage=data.get("stage", 1),
            skill_level=data.get("skill_level", 1),
            money=data.get("money", 0),
            orders_completed=data.get("orders_completed", 0),
            orders_failed=data.get("orders_failed", 0),
            orders_rejected=data.get("orders_rejected", 0)
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "stage": self.stage,
            "skill_level": self.skill_level,
            "money": self.money,
            "orders_completed": self.orders_completed,
            "orders_failed": self.orders_failed,
            "orders_rejected": self.orders_rejected
        }
