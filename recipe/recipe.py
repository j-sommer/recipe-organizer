from dataclasses import dataclass
from typing import List

from recipe.ingredient.ingredient import Ingredient


@dataclass
class Recipe:
    title: str
    labels: [str]
    ingredients: List[Ingredient]
    preparation: str
