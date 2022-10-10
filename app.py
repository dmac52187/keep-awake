import tkinter as tk
from tkinter import ttk
from settings import SettingsWindow, SettingsConfig
from autouser import AutoMouse, AutoType
from menubar import MenuBar


# main window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # window config
        self.geometry('300x200')
        self.title('Keep Awake')
        tk.Grid.columnconfigure(self, 2, weight=1)

        # MenuBar
        self.menuBar = MenuBar(None)

        # AutoType instance (widget)
        self.autoType = AutoType()

        # config instance (settings)
        self.settingsConfig = SettingsConfig()

        # start/stop/settings buttons
        startButton = ttk.Button(self, text="start", command=self.start)
        startButton.pack()

        stopButton = ttk.Button(self, text="stop", command=self.stop)
        stopButton.pack()

        settingsButton = ttk.Button(self, text='Settings', command=self.open_settings)
        settingsButton.pack()


    # main window functions
    def color_on(self):
        self.config(background='red')

    def color_off(self):
        self.config(background="SystemButtonFace")

    def start(self):
        # get settings
        self.autoType.text = self.settingsConfig.getSettings()
        self.autoType.type = True
        self.autoType.send_keys()
        self.color_on()

    def stop(self):
        self.autoType.type = False
        self.color_off()

    def open_settings(self):
        window = SettingsWindow(self)
        window.grab_set()

    def close(self):
        self.destroy()
        exit()


# run application
if __name__ == "__main__":
    app = App()
    app.config(menu=app.menuBar)
    app.protocol("WM_DELETE_WINDOW", app.close)
    app.mainloop()
