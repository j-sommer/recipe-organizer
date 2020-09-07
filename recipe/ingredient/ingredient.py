from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    quantity_type: str
    quantity: float
