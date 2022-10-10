import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

## menu bar


class MenuBar(Menu):
    def __init__(self, parent):
        super().__init__(parent)

        file = Menu(self, tearoff=False)
        settings = Menu(self, tearoff=False)
        for item in ('AutoType', 'AutoMouse'):
            settings.add_command(label=item)
        file.add_cascade(label='settings', menu=settings)
        self.add_cascade(label='File', menu=file)
        file.add_separator()
        file.add_command(label="Exit", underline=1, command=self.quit)


        help = Menu(self, tearoff=0)
        help.add_command(label="About", command=self.about)
        self.add_cascade(label="Help", menu=help)

    def exit(self):
        self.exit

    def about(self):
        messagebox.showinfo(
            'PythonGuides', 'Python Guides aims at providing best practical tutorials')
