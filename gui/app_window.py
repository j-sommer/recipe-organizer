from tkinter import Tk


class AppWindow:
    def __init__(self):
        self._window = Tk()
        self._window.title("Ingredient Extractor")
        self._window.state("zoomed")
        self._window.mainloop()
