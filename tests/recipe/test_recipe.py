from recipe_organizer.recipe.ingredient.ingredient import Ingredient
from recipe_organizer.recipe.recipe import Recipe


def test_recipe_serialization():
    # Given
    recipe = Recipe(
        "title",
        ["labelA", "labelB"],
        [Ingredient("name", "g", 50)],
        "preparation"
    )

    # When
    json_string = recipe.to_json()

    # Then
    assert "title" in json_string
    assert "labelA" in json_string
    assert "preparation" in json_string


def test_recipe_deserialization():
    # Given
    json_string = """{"py/object": "recipe_organizer.recipe.recipe.Recipe", "title": "title", "labels": ["labelA", "labelB"], "ingredients": [{"py/object": "recipe_organizer.recipe.ingredient.ingredient.Ingredient", "name": "name", "quantity_type": "g", "quantity": 50}], "preparation": "preparation"}"""

    # When
    actual: Recipe = Recipe.from_json(json_string)

    # Then
    assert actual.title == "title"
    assert actual.labels == ["labelA", "labelB"]
    assert actual.preparation == "preparation"
