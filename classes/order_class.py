from dataclasses import dataclass

@dataclass
class order_class:
    name: str
    quantity: int
    variation: list

    def __repr__(self):
        return (f"{self.name} - {self.quantity} - {self.variation}")