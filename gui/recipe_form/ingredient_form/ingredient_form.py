from tkinter import Frame, Entry


class IngredientForm(Frame):
    def __init__(self, parent, ingredient):
        super().__init__(parent)

        self._entry_ingredient_name = None
        self._entry_quantity = None
        self._entry_quantity_type = None

        self.define_widgets()
        self.define_layout()
        self.set_values(ingredient)

    def define_widgets(self):
        self._entry_ingredient_name = Entry(self)
        self._entry_quantity = Entry(self)
        self._entry_quantity_type = Entry(self)

    def define_layout(self):
        self._entry_ingredient_name.grid(row=0, column=0, pady=10, padx=5)
        self._entry_quantity.grid(row=0, column=1, padx=5)
        self._entry_quantity_type.grid(row=0, column=2)

    def set_values(self, ingredient):
        self._entry_ingredient_name.insert(0, ingredient.name)
        self._entry_quantity.insert(0, ingredient.quantity)
        self._entry_quantity_type.insert(0, ingredient.quantity_type)
