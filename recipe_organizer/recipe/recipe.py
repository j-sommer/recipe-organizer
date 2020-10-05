from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from recipe_organizer.recipe.ingredient.ingredient import Ingredient


@dataclass_json
@dataclass
class Recipe:
    title: str
    labels: List[str]
    ingredients: List[Ingredient]
    preparation: str
