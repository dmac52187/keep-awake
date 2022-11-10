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
        self.geometry('2000x800')
        self.title('Keep Awake')
        tk.Grid.columnconfigure(self, 2, weight=1)

        # MenuBar
        self.menuBar = MenuBar(self)

        # AutoType instance (widget)
        self.autoType = AutoType(self)

        # AutoMouse instance (widget)
        self.autoMouse = AutoMouse(self)

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
        # self.config(background="")

    def start(self):
        mode = int(self.menuBar.getMode())
        if mode == 1:
            # auto type
            self.autoType.text = self.settingsConfig.getSettings()
            self.autoType.type = True
            self.autoType.send_keys()
        elif mode == 2:
            # auto mouse
            self.autoMouse.move = True
            self.autoMouse.move_mouse()
        self.color_on()

    def stop(self):
        self.autoType.type = False
        self.autoMouse.move = False
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
    app.lift()
    app.attributes('-topmost', True)
    app.mainloop()
