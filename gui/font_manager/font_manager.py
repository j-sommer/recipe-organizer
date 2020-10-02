from tkinter import font


class FontManager:
    def __init__(self, root):
        self._root = root

    def set_default_font(self):
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=12)

        self._root.option_add("*Font", default_font)
