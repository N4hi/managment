from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import fills
from category import categoryClass
from fills import fillsClass
from create_db import initialize_database, insert_items, get_items, delete_item
import sqlite3

class add_items:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("الناهي للمبيعات")
        self.root.config(bg="white")
        self.root.focus_force()

        add_items_frame = Frame(self.root, bd=2, relief=RIDGE, bg= 'white')
        add_items_frame.place(x=700, y=10, width=450, height=480)

        #title
        title = Label(add_items_frame, text="تفاصيل المنتج", font=("times new roman",  15, 'bold'), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        lbl_category = Label(add_items_frame, text="المجموعة", font=("times new roman", 18), bg="white").place(x=300, y=60)
        combo_category = ttk.Combobox(add_items_frame)
        combo_category.set("اختار المجموعة")
        combo_category.place(x=100, y=60)

if __name__ == "__main__":
    root = Tk()
    items = add_items(root)
    root.mainloop()