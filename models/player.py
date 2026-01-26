class Player:
    def __init__(
        self,
        name: str,
        stage: int,
        money: int,
        orders_completed: int,
        orders_failed: int,
        orders_rejected: int
    ):
        self.name = name
        self.stage = stage
        self.money = money
        self.orders_completed = orders_completed
        self.orders_failed = orders_failed
        self.orders_rejected = orders_rejected

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", "Barista"),
            stage=data.get("stage", 1),
            money=data.get("money", 0),
            orders_completed=data.get("orders_completed", 0),
            orders_failed=data.get("orders_failed", 0),
            orders_rejected=data.get("orders_rejected", 0)
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "stage": self.stage,
            "money": self.money,
            "orders_completed": self.orders_completed,
            "orders_failed": self.orders_failed,
            "orders_rejected": self.orders_rejected
        }
