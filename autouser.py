from tkinter import *
import keyboard
import mouse


class AutoType(Frame):
    def __init__(self):
        Frame.__init__(self)
        self._count = 0
        self.delayTime = 1000
        self.type = False
        self.text = "hello"
        self._text = self.text
        self.label = Label(text="0")
        self.label.pack()
        self.entry = Entry(width=15)
        self.entry.pack()

    def send_keys(self):
        self.label.config(text=str(self._count))
        self.entry.focus()
        if self.type == True:
            self.label.config(background="green")
            self._count += 1
            self._text = self.text
            if self._count % 2 == 0:
               self.entry.delete(0, END)
            else:
                keyboard.write(self._text)
            self.after(self.delayTime, self.send_keys)
        else:
            self.label.config(background="SystemButtonFace")


class AutoMouse(Frame):
    def __init__(self):
        Frame.__init__(self)
        self._count = 0
        self.delayTime = 1000
        self.moveDuration = .2
        self.moveDistanceX = 100
        self.moveDistanceY = 0
        self.move = False
        self.label = Label(text="0")
        self.label.pack()

    def move_mouse(self):
        self.label.config(text=str(self._count))
        if self.move == True:
            self.label.config(background="green")
            self._count += 1
            x = self.moveDistanceX
            y = self.moveDistanceY
            if self._count % 2 == 0:
                x = -self.moveDistanceX
                y = -self.moveDistanceY
            mouse.move(x, y, absolute=False, duration=self.moveDuration)
            self.after(self.delayTime, self.move_mouse)
        else:
            self.label.config(background="SystemButtonFace")
