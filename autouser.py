from tkinter import *
import keyboard
import mouse


class AutoType(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self._count = 0
        self.delayTime = 1000
        self.type = False
        self.text = "hello"
        self._text = self.text
        self.Label = Label(text="Auto Type Mode")
        self.Label.pack()
        self.countLabel = Label(text="0")
        self.countLabel.pack()
        self.entry = Entry(width=15)
        self.entry.pack()


    def hide(self):
        self.Label.pack_forget()
        self.countLabel.pack_forget()
        self.entry.pack_forget()

    def show(self):
        self.Label.pack()
        self.countLabel.pack()
        self.entry.pack()

    def send_keys(self):
        self.countLabel.config(text=str(self._count))
        self.entry.focus()
        if self.type == True:
            self.countLabel.config(background="green")
            self._count += 1
            self._text = self.text
            if self._count % 2 == 0:
               self.entry.delete(0, END)
            else:
                keyboard.write(self._text)
            self.after(self.delayTime, self.send_keys)
        else:
            self.countLabel.config(background="SystemButtonFace")


class AutoMouse(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self._count = 0
        self.delayTime = 1000
        self.moveDuration = .2
        self.moveDistanceX = 100
        self.moveDistanceY = 0
        self.move = False
        self.Label = Label(text="Auto Mouse Mode")
        self.Label.pack()
        self.countLabel = Label(text="0")
        self.countLabel.pack()


    def hide(self):
        self.Label.pack_forget()
        self.countLabel.pack_forget()

    def show(self):
        self.Label.pack()
        self.countLabel.pack()
    
    def move_mouse(self):
        self.countLabel.config(text=str(self._count))
        if self.move == True:
            self.countLabel.config(background="green")
            self._count += 1
            x = self.moveDistanceX
            y = self.moveDistanceY
            if self._count % 2 == 0:
                x = -self.moveDistanceX
                y = -self.moveDistanceY
            mouse.move(x, y, absolute=False, duration=self.moveDuration)
            self.after(self.delayTime, self.move_mouse)
        else:
            self.countLabel.config(background="SystemButtonFace")
