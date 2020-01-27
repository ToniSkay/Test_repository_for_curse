
from tkinter import *

class Apple(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_interface()

    def create_interface(self):
        Label(self, text = 'Your like kinofilm').grid(row = 0, column = 0, sticky = W)
        Label(self, text = 'Choose only one, please!').grid(row = 1, column = 0, sticky = W)
        self.favorite = StringVar()
        self.favorite.set(None)
        Radiobutton(self, text = 'Matrix', variable = self.favorite,
                    value = 'Matrix', command = self.update_but).grid(row = 2, column = 0, sticky = W)
        Radiobutton(self, text = 'Star Wars', variable = self.favorite,
                    value = 'Star Wars', command = self.update_but).grid(row = 3, column = 0, sticky = W)
        self.txt = Text(self, width = 20, height = 4, wrap = WORD)
        self.txt.grid(row = 4, column = 0, columnspan = 2, sticky = W)

    def update_but(self):
        message = "Your liked film - "
        message += self.favorite.get()
        self.txt.delete(0.0, END)
        self.txt.insert(0.0, message)

root = Tk()
root.title('Da poxer')
root.geometry('500x500')
app = Apple(root)
root.mainloop()