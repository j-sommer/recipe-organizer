from dataclasses import dataclass
from typing import List

from jsonpickle import encode, decode

from recipe_organizer.recipe.ingredient.ingredient import Ingredient


@dataclass
class Recipe:
    title: str
    labels: [str]
    ingredients: List[Ingredient]
    preparation: str

    def to_json(self) -> str:
        return encode(self)

    @staticmethod
    def from_json(json):
        return decode(json)