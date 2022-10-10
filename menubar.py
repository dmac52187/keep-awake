import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

## menu bar


class MenuBar(Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.modeType = BooleanVar()
        self.modeMouse = BooleanVar()

        self.autoMode = StringVar()
        self.autoMode.set(1)

        self.modes = {
            'AutoType': 1,
            'AutoMouse': 2
        }

        file = Menu(self, tearoff=False)
        mode = Menu(self, tearoff=False)
        for k,v in self.modes.items():
            mode.add_radiobutton(label=k,value=v,variable=self.autoMode)
        file.add_cascade(label='Mode', menu=mode)
        self.add_cascade(label='File', menu=file)
        file.add_separator()
        file.add_command(label="Exit", underline=1, command=self.quit)


        help = Menu(self, tearoff=0)
        help.add_command(label="About", command=self.about)
        self.add_cascade(label="Help", menu=help)

    def getMode(self):
        return self.autoMode.get()

    def exit(self):
        self.exit

    def about(self):
        # print(self.autoMode.get())
        messagebox.showinfo(
            'PythonGuides', 'Python Guides aims at providing best practical tutorials')
