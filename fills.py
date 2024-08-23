import sqlite3
from tkinter import *
from tkinter import messagebox
from create_db import initialize_database, insert_items, get_items, delete_item

class fillsClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x750+220+130")
        self.root.title("الناهي للمبيعات")
        self.root.config(bg="white")


        #initialize database
        initialize_database()

        # all variables
        self.var_srch = StringVar()


        # Initialize components
        srch_bar = Entry(self.root, textvariable=self.var_srch, bd=2, bg="white", fg="#1E2A5E", justify=CENTER, relief=RIDGE, font=("arial", 18))
        srch_bar.place(x=350, y=40, width=500)
        srch_lbl = Button(self.root, text="البحث", bg="white", fg='#1E2A5E', font=("arial", 20)).place(x=900, y=40)
        srch_bar.bind("<KeyRelease>", self.search_items)

        # Listbox 
        self.list_box = Listbox(self.root, bd=2, bg="white", borderwidth=2, relief=RIDGE)
        self.list_box.place(x=350, y=120, width=500, height=500)

        self.scrly = Scrollbar(self.list_box, orient=VERTICAL)
        self.scrly.pack(side=RIGHT, fill=Y)
        self.scrly.config(command=self.list_box.yview)

        add_btn = Button(self.root, text="اضافة", cursor="hand2", command=self.add_fil, font=("times new roman", 15, "bold"), bg='#1E2A5E', fg="white")
        add_btn.place(x=750, y=630, width=100, height=50)

        remove_btn = Button(self.root, text="حذف", cursor="hand2", command=self.remove_btn, font=("times new roman", 15, "bold"), bg='red', fg="white")
        remove_btn.place(x=630, y=630, width=100, height=50)

        #load existing items
        self.load_items()

    def remove_btn(self):
        selected_item = self.list_box.curselection()
        if selected_item:
            item_name = self.list_box.get(selected_item)
            confirm = messagebox.askyesno("تأكيد", f"هل أنت متأكد أنك تريد حذف '{item_name}'؟", parent=self.root)
            if confirm:
                delete_item(item_name)
                self.load_items()
                messagebox.showinfo("نجاح", "تم حذف العنصر بنجاح", parent=self.root)
        else:
            messagebox.showwarning("تحذير", "من فضلك اختر عنصرًا لحذفه", parent=self.root)

    def add_fil(self):
        self.new_win = Toplevel(self.root)
        self.new_win.geometry("600x600+500+130")
        self.new_win.title("اضافة تعبئات")
        self.new_win.focus_force()

        srch1_bar = Entry(self.new_win, bd=2, bg="white", fg="#1E2A5E", justify=CENTER, relief=RIDGE, font=("arial", 18))
        srch1_bar.place(x=100, y=50, width=300)

        def save_item():
            item_name = srch1_bar.get()
            if item_name:
                insert_items(item_name)
                messagebox.showinfo("Sucess", "تم اضافة التعبئة بنجاح", parent=self.root)
                srch1_bar.delete(0, END)
                self.load_items()

        add1_btn = Button(self.new_win, text="اضافة", cursor="hand2", command=save_item, font=("times new roman", 25, "bold"), bg='#1E2A5E', fg="white")
        add1_btn.place(x=450, y=40, width=100, height=50)

    def load_items(self):
        self.list_box.delete(0, END)
        items = get_items()
        for item in items:
            self.list_box.insert(END, item[0])
       
    
    def search_items(self, event):
        search_text = self.var_srch.get().strip()

        conn = sqlite3.connect('items.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM items WHERE name LIKE ?", ('%' + search_text + '%',))
        items = cursor.fetchall()
        conn.close()

        self.list_box.delete(0, END)
        for item in items:
            self.list_box.insert(END, item[0])


if __name__ == "__main__":
    root = Tk()
    fil = fillsClass(root)
    root.mainloop()
