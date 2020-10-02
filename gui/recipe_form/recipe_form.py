from tkinter import Label, Entry, END, Frame, Text, Button, W, E
from typing import Any, Callable

from events.event import Event, EventType
from events.event_observer import EventObserver
from events.event_publisher import EventPublisher
from gui.interfaces.list_item_holder import ListItemHolder
from gui.interfaces.widget_container import WidgetContainer
from gui.recipe_form.form_label.form_label import FormLabel
from gui.recipe_form.ingredient_form.ingredient_form import IngredientForm
from recipe.ingredient.ingredient import Ingredient
from recipe.recipe import Recipe


class RecipeForm(Frame, WidgetContainer, EventObserver, ListItemHolder):
    _label_title: Label
    _entry_title: Entry
    _frame_ingredients: Frame
    _label_ingredients: Label
    _label_preparation: Label
    _text_preparation: Text
    _button_save: Button
    _button_add_ingredient: Button

    _ingredient_forms: [IngredientForm] = []

    _event_handler = {
        EventType.FILE_READ: Callable
    }

    def __init__(self):
        super().__init__()

        EventPublisher.add(self)

        self._event_handler[EventType.FILE_READ] = self.set_values

    def notify(self, event: Event) -> None:
        if event.event_type in self._event_handler:
            self._event_handler.get(event.event_type)(event.payload)

    def remove_item(self, to_remove: Any) -> None:
        requested_index = self._ingredient_forms.index(to_remove)
        self._ingredient_forms[requested_index].destroy()
        self._ingredient_forms.remove(to_remove)

    def define_widgets(self) -> None:
        self._label_title = FormLabel(self, text="Titel")
        self._entry_title = Entry(self)
        self._label_ingredients = FormLabel(self, text="Zutaten")
        self._frame_ingredients = Frame(self)
        self._label_preparation = FormLabel(self, text="Zubereitung")
        self._text_preparation = Text(self)
        self._button_add_ingredient = Button(self, text="hinzufügen", command=self.add_ingredient)

    def define_layout(self) -> None:
        self._label_title.grid(row=0)
        self._entry_title.grid(row=1, sticky=W + E)
        self._label_ingredients.grid(row=2, column=0)
        self._frame_ingredients.grid(row=3)
        self._button_add_ingredient.grid(row=4)
        self._label_preparation.grid(row=5, column=0)
        self._text_preparation.grid(row=6)

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

    def get_recipe_from_form(self) -> Recipe:
        return Recipe(
            self._entry_title.get(),
            [],
            [form.get_ingredient() for form in self._ingredient_forms],
            self._text_preparation.get("1.0", END))
