import tkinter as tk
from tkinter import ttk
from tkinter import *
import json

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x200')
        self.title('Toplevel Window')
        self.title("Settings")
        # tk.self.eval('tk::PlaceWindow . center')  # center window


        # data
        self.autoTextLabel = ttk.Label(self)
        self.autoTextLabel.pack()
        self.autoTextLabel.config(text="Text: ")

        textVar = SettingsConfig.getSettings(self)
        autoTextInput = ttk.Entry(self, width=15, textvariable=textVar)
        autoTextInput.insert(END, textVar)
        autoTextInput.pack()

        saveButton = ttk.Button(self,  text='Save', command=lambda: SettingsConfig.saveSettings(
           self,  autoTextInput.get(), self.destroy()))
        saveButton.pack()

        closeButton = ttk.Button(self,  text='Close', command=self.destroy)
        closeButton.pack()


class SettingsConfig():
    def __init__(self):
        self.text = "default"

    def getSettings(self):
        with open('keep_awake.config.json') as j:
            config = json.load(j)

            # config variables
            text = config['text']
            return text

    # def saveSettings(text, callback):
    def saveSettings(self, text, callback):
        f = open("keep_awake.config.json", "r")
        config = json.load(f)
        f.close()

        config['text'] = text
        self.text = text

        f = open("keep_awake.config.json", "w")
        json.dump(config, f)
        f.close()
        callback
