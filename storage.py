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
        self.root.geometry("1100x600+220+130")
        self.root.title("الناهي للمبيعات")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_itemtype = StringVar()
        self.var_itemname = StringVar()
        self.var_buycur = StringVar()
        self.var_sellcur = StringVar()
        self.var_fil1 = StringVar()
        self.var_fil2 = StringVar()
        self.var_numitem = StringVar()
        self.var_buyitem = StringVar()
        self.var_sellitem = StringVar()
        self.var_num2item = StringVar()
        self.var_buy2item = StringVar()
        self.var_sell2item = StringVar()
        self.var_num = StringVar()
        self.var_buy = StringVar()
        self.var_sell = StringVar
        
        add_items_frame = Frame(self.root, bd=2, relief=RIDGE, bg= 'white')
        add_items_frame.place(x=600, y=10, width=550, height=600)

        #title
        title = Label(add_items_frame, text="تفاصيل المنتج", font=("times new roman",  15, 'bold'), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)
        #column 1
        self.lbl_category = Label(add_items_frame, text="المجموعة", font=("times new roman", 18), bg="white").place(x=400, y=60)
        self.lbl_supplier = Label(add_items_frame, text="اسم الموزع", font=("times new roman", 18), bg="white").place(x=400, y=110)
        self.lbl_itemtype = Label(add_items_frame, text="نوع المادة", font=("times new roman", 18), bg="white").place(x=400, y=160)
        self.lbl_itemname = Label(add_items_frame, text="اسم المادة", font=("times new roman", 18), bg="white").place(x=400, y=210)
        self.lbl_buycur = Label(add_items_frame, text="عملة الشراء", font=("times new roman", 18), bg="white").place(x=390, y=260)
        self.lbl_sellcur= Label(add_items_frame, text="عملة البيع", font=("times new roman", 18), bg="white").place(x=200, y=260)
        self.lbl_fil1 = Label(add_items_frame, text="تعبئة 1 ", font=("times new roman", 18), bg="white")
        self.lbl_fil2 = Label(add_items_frame, text="تعبئة 2", font=("times new roman", 18), bg="white")
        self.lbl_numitem = Label(add_items_frame, text="عدد الطول", font=("times new roman", 18), bg="white")
        self.lbl_buyitem = Label(add_items_frame, text="شراء الطول", font=("times new roman", 18), bg="white")
        self.lbl_sellitem = Label(add_items_frame, text="بيع الطول ", font=("times new roman", 18), bg="white")
        self.lbl_num2item = Label(add_items_frame, text="عدد الطول", font=("times new roman", 18), bg="white")
        self.lbl_buy2item = Label(add_items_frame, text="شراء الطول", font=("times new roman", 18), bg="white")
        self.lbl_sell2item = Label(add_items_frame, text="بيع الطول ", font=("times new roman", 18), bg="white")
        self.lbl_num = Label(add_items_frame, text="العدد", font=("times new roman", 18), bg="white")
        self.lbl_buy = Label(add_items_frame, text="سعر الشراء", font=("times new roman", 18), bg="white")
        self.lbl_sell = Label(add_items_frame, text="سعر البيع", font=("times new roman", 18), bg="white")
        #column 2

        cmb_category = ttk.Combobox(add_items_frame, textvariable=self.var_cat, values=("اختار"), state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_category.place(x=150, y=60, width=200)
        cmb_category.current(0)

        txt_sup = Entry(add_items_frame, textvariable=self.var_sup, bd=2, font=("times new roman", 15)).place(x=150, y=110, width=200)

        
        cmb_fill = ttk.Combobox(add_items_frame, textvariable=self.var_itemtype, values=("اختار", "اعتيادية", "معبئة"), state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_fill.place(x=150, y=160, width=200)
        cmb_fill.current(0)
        cmb_fill.bind("<<ComboboxSelected>>", self.update_labels)

        
    def update_labels(self, event):
        selected_value = self.var_itemtype.get()

        self.lbl_fil1.place_forget()
        self.lbl_fil2.place_forget()
        self.lbl_numitem.place_forget()
        self.lbl_buyitem.place_forget()
        self.lbl_sellitem.place_forget()
        self.lbl_num2item.place_forget()
        self.lbl_buy2item.place_forget()
        self.lbl_sell2item.place_forget()
        self.lbl_num.place_forget()
        self.lbl_buy.place_forget()
        self.lbl_sell.place_forget()

        if selected_value == "معبئة":

            self.lbl_fil1.place(x=390, y=310)
            self.lbl_fil2.place(x=110, y=310)
            self.lbl_numitem.place(x=400, y=360)
            self.lbl_buyitem.place(x=390, y=410)
            self.lbl_sellitem.place(x=400, y=460)
            self.lbl_num2item.place(x=150, y=360)
            self.lbl_buy2item.place(x=150, y=410)
            self.lbl_sell2item.place(x=150, y=460)

        else:
            
            self.lbl_num.place(x=400, y=400)
            self.lbl_buy.place(x=400, y=450)
            self.lbl_sell.place(x=400, y=500)


if __name__ == "__main__":
    root = Tk()
    items = add_items(root)
    root.mainloop()