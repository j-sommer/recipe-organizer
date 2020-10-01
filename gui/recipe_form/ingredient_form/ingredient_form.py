from tkinter import Frame, Entry, Button

from gui.interfaces.list_item_holder import ListItemHolder
from gui.interfaces.widget_container import WidgetContainer
from recipe.ingredient.ingredient import Ingredient


class IngredientForm(Frame, WidgetContainer):
    _list_holder: ListItemHolder

    _entry_ingredient_name: Entry
    _entry_quantity: Entry
    _entry_quantity_type: Entry
    _button_remove: Button

    def __init__(self, parent, ingredient, list_holder: ListItemHolder):
        super().__init__(parent)

        self._list_holder = list_holder

        self.define_widgets()
        self.define_layout()
        self.set_values(ingredient)

    def define_widgets(self) -> None:
        self._entry_ingredient_name = Entry(self)
        self._entry_quantity = Entry(self)
        self._entry_quantity_type = Entry(self)
        self._button_remove = Button(self, text="entfernen", command=self.remove_ingredient)

    def define_layout(self) -> None:
        self._entry_ingredient_name.grid(row=0, column=0, pady=10, padx=5)
        self._entry_quantity.grid(row=0, column=1, padx=5)
        self._entry_quantity_type.grid(row=0, column=2)
        self._button_remove.grid(row=0, column=3)

    def set_values(self, ingredient) -> None:
        self._entry_ingredient_name.insert(0, ingredient.name)
        self._entry_quantity.insert(0, ingredient.quantity)
        self._entry_quantity_type.insert(0, ingredient.quantity_type)

    def get_ingredient(self) -> Ingredient:
        return Ingredient(
            self._entry_ingredient_name.get(),
            self._entry_quantity_type.get(),
            self._entry_quantity.get()
        )

    def remove_ingredient(self):
        self._list_holder.remove_item(self)
