class Player:
    def __init__(
        self,
        name: str,
        stage: int,
        skill_level: int,
        money: int,
        total_money_earned: int,
        has_leveled_up_today: bool,
        orders_completed: int,
        orders_failed: int,
        orders_rejected: int,
        inventory: dict | None = None,
        storage_capacity: int = 20,
    ):
        self.name = name
        self.stage = stage
        self.skill_level = skill_level
        self.money = money
        self.total_money_earned = total_money_earned
        self.has_leveled_up_today = has_leveled_up_today
        self.orders_completed = orders_completed
        self.orders_failed = orders_failed
        self.orders_rejected = orders_rejected
        self.inventory = inventory if inventory is not None else {}
        self.storage_capacity = storage_capacity

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", "Barista"),
            stage=data.get("stage", 1),
            skill_level=data.get("skill_level", 1),
            money=data.get("money", 0),
            total_money_earned=data.get("total_money_earned", 0),
            has_leveled_up_today=data.get("has_leveled_up_today", False),
            orders_completed=data.get("orders_completed", 0),
            orders_failed=data.get("orders_failed", 0),
            orders_rejected=data.get("orders_rejected", 0),
            storage_capacity=data.get("storage_capacity", 20)
        )

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "stage": self.stage,
            "skill_level": self.skill_level,
            "money": self.money,
            "total_money_earned": self.total_money_earned,
            "has_leveled_up_today": self.has_leveled_up_today,
            "orders_completed": self.orders_completed,
            "orders_failed": self.orders_failed,
            "orders_rejected": self.orders_rejected,
            "storage_capacity": self.storage_capacity
        }
