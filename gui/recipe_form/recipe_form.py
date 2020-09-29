from tkinter import Label, Entry, END, Frame, Text, Button

from gui.recipe_form.ingredient_form.ingredient_form import IngredientForm
from recipe.events.recipe_event import RecipeEvent, RecipeEventType
from recipe.events.recipe_event_observer import RecipeEventObserver
from recipe.events.recipe_event_publisher import RecipeEventPublisher
from recipe.recipe import Recipe


class RecipeForm(Frame, RecipeEventObserver):
    def __init__(self):
        super().__init__()

        self._label_title = None
        self._entry_title = None
        self._frame_ingredients = None
        self._label_ingredients = None
        self._label_preparation = None
        self._text_preparation = None
        self._button_save = None

        self._ingredient_forms = []

        RecipeEventPublisher.add(self)

    def notify(self, event: RecipeEvent) -> None:
        if event.event_type == RecipeEventType.READ:
            self.set_values(event.payload)

    def define_widgets(self):
        self._label_title = Label(self, text="Titel")
        self._entry_title = Entry(self)
        self._label_ingredients = Label(self, text="Zutaten")
        self._frame_ingredients = Frame(self)
        self._label_preparation = Label(self, text="Zubereitung")
        self._text_preparation = Text(self)
        self._button_save = Button(self, text="speichern", command=self.save_recipe)

    def configure_layout(self):
        pass

    def define_layout(self):
        self._label_title.grid(row=0, column=0)
        self._entry_title.grid(row=0, column=1)
        self._label_ingredients.grid(row=1, column=0)
        self._frame_ingredients.grid(row=2)
        self._label_preparation.grid(row=3, column=0)
        self._text_preparation.grid(row=4)
        self._button_save.grid(row=5)

    def set_values(self, recipe):
        if recipe:
            self.define_widgets()
            self.define_layout()

            self._entry_title.insert(0, recipe.title)

            for index, ingredient in enumerate(recipe.ingredients):
                self.define_ingredient_form(index, ingredient)

            self._text_preparation.insert(END, recipe.preparation)

    def define_ingredient_form(self, position, ingredient):
        ingredient_form = IngredientForm(self._frame_ingredients, ingredient)
        ingredient_form.grid(row=position)

        self._ingredient_forms.append(ingredient_form)

    def get_recipe(self):
        ingredients = [form.get_ingredient() for form in self._ingredient_forms]
        return Recipe(
            self._entry_title.get(),
            [],
            ingredients,
            self._text_preparation.get("1.0", END)
        )

    def save_recipe(self):
        RecipeEventPublisher.broadcast(RecipeEvent(RecipeEventType.SAVE, payload=self.get_recipe()))
