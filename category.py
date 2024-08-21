from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("الناهي للمبيعات")
        self.root.config(bg="white")
        self.root.focus_force()


if __name__=="__main__":
    root=Tk()
    inv = categoryClass(root)
    root.mainloop()
