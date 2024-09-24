import sqlite3
from tkinter import *
from tkinter import messagebox
from create_db import initialize_database, insert_items, get_items, delete_item , insert_groups , get_groups , delete_group

class categoryClass:
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
        srch_bar.bind("<KeyRelease>", self.search_group)

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
        self.load_groups()

    



    #window add new_item
    def add_fil(self):
        self.new_win = Toplevel(self.root)
        self.new_win.geometry("600x600+500+130")
        self.new_win.title("اضافة تعبئات")
        self.new_win.focus_force()

        srch1_bar = Entry(self.new_win, bd=2, bg="white", fg="#1E2A5E" ,   justify=CENTER, relief=RIDGE, font=("arial", 18))
        srch1_bar.place(x=100, y=50, width=200)
        
        group_add = Entry(self.new_win, bd=2, bg="white", fg="#1E2A5E" ,   justify=CENTER, relief=RIDGE, font=("arial", 18))
        group_add.place(x=100, y=100, width=200)
        group_add.insert(0 , "اسم المجموعة")

        #price_add = Entry(self.new_win, bd=2, bg="white", fg="#1E2A5E" ,   justify=CENTER, relief=RIDGE, font=("arial", 18))
        #price_add.place(x=100, y=150, width=200)
        #price_add.insert(0 , "سعر العنصر")
#
#
        #quantity_add = Entry(self.new_win, bd=2, bg="white", fg="#1E2A5E" ,   justify=CENTER, relief=RIDGE, font=("arial", 18))
        #quantity_add.place(x=100, y=200, width=200)
        #quantity_add.insert(0 , "العدد")
#
#
        #sell_add = Entry(self.new_win, bd=2, bg="white", fg="#1E2A5E" ,   justify=CENTER, relief=RIDGE, font=("arial", 18))
        #sell_add.place(x=100, y=250, width=200)
        #sell_add.insert(0 , "سعر البيع")
#
#
        #buy_add = Entry(self.new_win, bd=2, bg="white", fg="#1E2A5E" ,   justify=CENTER, relief=RIDGE, font=("arial", 18))
        #buy_add.place(x=100, y=300, width=200)
        #buy_add.insert(0 , "سعر الشراء")
#
#
        #group_add1 = Entry(self.new_win, bd=2, bg="white", fg="#1E2A5E" ,   justify=CENTER, relief=RIDGE, font=("arial", 18))
        #group_add1.place(x=100, y=350, width=200)
        #group_add1.insert(0 , "المجموعة")




        def save_groups():
            group_name = group_add.get().strip()
            #price_item = price_add.get()
            #quantity_item = quantity_add.get()
            #sell_item = sell_add.get()
            #buy_item = buy_add.get()
            #group_item = group_add.get()
            if group_name:
                insert_groups(group_name )
                messagebox.showinfo("Sucess", "تم اضافة التعبئة بنجاح", parent=self.root)
                group_add.delete(0 , END)
                self.load_groups()


        add1_btn = Button(self.new_win, text="sssssssاضافة", cursor="hand2", command=save_groups, font=("times new roman", 25, "bold"), bg='#1E2A5E', fg="white")
        add1_btn.place(x=450, y=40, width=100, height=50)

        #end window new_item


    #fun is  used to load items from database 
    def load_groups(self):
        self.list_box.delete(0, END)
        groups =get_groups()
        if groups is None:
            messagebox.showerror("Error", "لا يوجد عناصر", parent=self.root)
            return
        for group in groups:
            self.list_box.insert(END, group[0])

          
            
    #fun is  used to delete item from database
    def remove_btn(self):
        selected_item = self.list_box.curselection()
        if selected_item:
            group_name = self.list_box.get(selected_item)
            confirm = messagebox.askyesno("تأكيد", f"هل أنت متأكد أنك تريد حذف '{group_name}'؟", parent=self.root)
            if confirm:
                delete_group(group_name)
                self.load_groups()
                messagebox.showinfo("نجاح", "تم حذف العنصر بنجاح", parent=self.root)
        else:
            messagebox.showwarning("تحذير", "من فضلك اختر عنصرًا لحذفه", parent=self.root)





       
            
       
    
    def search_group(self, event):
        search_text = self.var_srch.get().strip()  # Removes extra spaces from the search bar
        conn = sqlite3.connect('items.db')
        cursor = conn.cursor()
        cursor.execute("SELECT group_name FROM groups WHERE group_name LIKE ?", ('%' + search_text + '%',))
        groups = cursor.fetchall()
        conn.close()

        self.list_box.delete(0, END)  # Clears the listbox first
        for group in groups:
            self.list_box.insert(END, group[0])  # Inserts the matched items



if __name__ == "__main__":
    root = Tk()
    fil = categoryClass(root)
    root.mainloop()
