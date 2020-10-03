from tkinter import Label, Entry, END, Frame, Text, Button, W, E
from typing import Any

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

    def __init__(self):
        super().__init__()

        self.define_widgets()
        self.define_layout()

        EventPublisher.add(self)

    def notify(self, event: Event) -> None:
        if event.event_type == EventType.FILE_READ:
            self.set_form_values(event.payload)

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
        self._button_add_ingredient = Button(self, text="hinzufügen", command=self.__add_ingredient)

    def define_layout(self) -> None:
        self._label_title.grid(row=0)
        self._entry_title.grid(row=1, sticky=W + E)
        self._label_ingredients.grid(row=2, column=0)
        self._frame_ingredients.grid(row=3)
        self._button_add_ingredient.grid(row=4)
        self._label_preparation.grid(row=5, column=0)
        self._text_preparation.grid(row=6)

    def set_form_values(self, recipe: Recipe) -> None:
        self.clear_form()

        if recipe:
            self._entry_title.insert(0, recipe.title)

            for index, ingredient in enumerate(recipe.ingredients):
                self.__define_ingredient_form(index, ingredient)

            self._text_preparation.insert(END, recipe.preparation)

    def get_recipe_from_form(self) -> Recipe:
        return Recipe(
            self._entry_title.get(),
            [],
            [form.get_ingredient() for form in self._ingredient_forms],
            self._text_preparation.get("1.0", END))

    def clear_form(self) -> None:
        self._entry_title.delete(0, END)

        for ingredient_form in self._ingredient_forms:
            ingredient_form.grid_forget()
            ingredient_form.destroy()

        self._ingredient_forms.clear()
        self._text_preparation.delete(1.0, END)

    def __define_ingredient_form(self, position: int, ingredient: Ingredient) -> None:
        ingredient_form = IngredientForm(self._frame_ingredients, ingredient, self)
        ingredient_form.grid(row=position)

        self._ingredient_forms.append(ingredient_form)

    def __add_ingredient(self) -> None:
        new_ingredient_form = IngredientForm(self._frame_ingredients, Ingredient("", "", 0), self)
        new_ingredient_form.grid(row=len(self._ingredient_forms))

        self._ingredient_forms.append(new_ingredient_form)
