from tkinter import Label


class FormLabel(Label):
    def __init__(self, *args, **kwargs):
        super(FormLabel, self).__init__(*args, **kwargs, pady=10)
