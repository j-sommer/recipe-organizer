from tkinter import OptionMenu, StringVar


class QuantityType(OptionMenu):
    OPTIONS = [
        "g",
        "ml",
        "EL"
    ]

    def __init__(self, parent):
        self._selection = StringVar(parent)
        self._selection.set(self.OPTIONS[0])

        OptionMenu.__init__(self, parent, self._selection, *self.OPTIONS)

    def get(self):
        return self._selection.get()

    def set(self, selection: str):
        self._selection.set(selection)
