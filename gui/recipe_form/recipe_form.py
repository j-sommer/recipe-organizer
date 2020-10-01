from tkinter import Label, Entry, END, Frame, Text, Button
from typing import Any

from gui.list_item_holder import ListItemHolder
from gui.recipe_form.ingredient_form.ingredient_form import IngredientForm
from recipe.events.recipe_event import RecipeEvent, RecipeEventType
from recipe.events.recipe_event_observer import RecipeEventObserver
from recipe.events.recipe_event_publisher import RecipeEventPublisher
from recipe.ingredient.ingredient import Ingredient
from recipe.recipe import Recipe


class RecipeForm(Frame, RecipeEventObserver, ListItemHolder):
    _label_title: Label
    _entry_title: Entry
    _frame_ingredients: Frame
    _label_ingredients: Label
    _label_preparation: Label
    _text_preparation: Text
    _button_save: Button
    _button_add_ingredient: Button

    _ingredient_forms: [IngredientForm] = []

    def __init__(self):
        super().__init__()

        RecipeEventPublisher.add(self)

    def notify(self, event: RecipeEvent) -> None:
        if event.event_type == RecipeEventType.READ:
            self.set_values(event.payload)

    def remove_item(self, to_remove: Any) -> None:
        requested_index = self._ingredient_forms.index(to_remove)
        self._ingredient_forms[requested_index].destroy()
        self._ingredient_forms.remove(to_remove)

    def define_widgets(self) -> None:
        self._label_title = Label(self, text="Titel")
        self._entry_title = Entry(self)
        self._label_ingredients = Label(self, text="Zutaten")
        self._frame_ingredients = Frame(self)
        self._label_preparation = Label(self, text="Zubereitung")
        self._text_preparation = Text(self)
        self._button_save = Button(self, text="speichern", command=self.save_recipe)
        self._button_add_ingredient = Button(self, text="hinzufügen", command=self.add_ingredient)

    def define_layout(self) -> None:
        self._label_title.grid(row=0, column=0)
        self._entry_title.grid(row=0, column=1)
        self._label_ingredients.grid(row=1, column=0)
        self._frame_ingredients.grid(row=2)
        self._button_add_ingredient.grid(row=3, column=1)
        self._label_preparation.grid(row=4, column=0)
        self._text_preparation.grid(row=5)
        self._button_save.grid(row=6)

    def set_values(self, recipe: Recipe) -> None:
        if recipe:
            self.define_widgets()
            self.define_layout()

            self._entry_title.insert(0, recipe.title)

            for index, ingredient in enumerate(recipe.ingredients):
                self.define_ingredient_form(index, ingredient)

            self._text_preparation.insert(END, recipe.preparation)

    def define_ingredient_form(self, position: int, ingredient: Ingredient) -> None:
        ingredient_form = IngredientForm(self._frame_ingredients, ingredient, self)
        ingredient_form.grid(row=position)

        self._ingredient_forms.append(ingredient_form)

    def add_ingredient(self) -> None:
        new_ingredient_form = IngredientForm(self._frame_ingredients, Ingredient("", "", 0), self)
        new_ingredient_form.grid(row=len(self._ingredient_forms))

        self._ingredient_forms.append(new_ingredient_form)

    def save_recipe(self) -> None:
        recipe = Recipe(
            self._entry_title.get(),
            [],
            [form.get_ingredient() for form in self._ingredient_forms],
            self._text_preparation.get("1.0", END))
        RecipeEventPublisher.broadcast(RecipeEvent(RecipeEventType.SAVE, payload=recipe))
