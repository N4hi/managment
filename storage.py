from tkinter import *
from tkinter import ttk, messagebox 
import sqlite3
import fills
from category import categoryClass
from fills import fillsClass
from create_db import initialize_database, insert_items, get_items, delete_item , get_groups
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

        #فورما الاعتيادي
        self.var_name = StringVar()
        self.var_num = StringVar()
        self.var_buyitem = StringVar()
        self.var_sellitem = StringVar()
        self.var_fil1 = StringVar()
        self.var_fil2 = StringVar()
        self.var_group = StringVar()
        ###########################
        
       #المعبئة
        self.var_num2item = StringVar()
        self.var_buy2item = StringVar()
        self.var_sell2item = StringVar()
        self.var_num = StringVar()
        self.var_num2 = StringVar()
        self.var_buy = StringVar()
        self.var_sell = StringVar()
        self.data_from_db = StringVar()
        self.var_spinebox = StringVar()
        
        add_items_frame = Frame(self.root, bd=2, relief=RIDGE, bg= 'white')
        add_items_frame.place(x=600, y=10, width=550, height=600)

        #title
        title = Label(add_items_frame, text="تفاصيل المنتج", font=("times new roman",  15, 'bold'), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)
        self.lbl_category = Label(add_items_frame, text="المجموعة", font=("times new roman", 18), bg="white").place(x=400, y=60)
        self.lbl_supplier = Label(add_items_frame, text="اسم الموزع", font=("times new roman", 18), bg="white").place(x=400, y=110)
        self.lbl_itemtype = Label(add_items_frame, text="نوع المادة", font=("times new roman", 18), bg="white").place(x=400, y=160)

        #label [الاعتيادي]        
        self.lbl_name = Label(add_items_frame, text="اسم المادة", font=("times new roman", 18), bg="white").place(x=400, y=210)
        self.lbl_num = Label(add_items_frame, text="العدد", font=("times new roman", 18), bg="white")
        self.lbl_buy = Label(add_items_frame, text="سعر الشراء", font=("times new roman", 18), bg="white")
        self.lbl_sell = Label(add_items_frame, text="سعر البيع", font=("times new roman", 18), bg="white")
        self.lbl_groups = Label(add_items_frame, text="المجموعة", font=("times new roman", 18), bg="white")

         #entries1 [الاعتيادي]
        self.ent_name = Entry(add_items_frame, bd=2, textvariable= self.var_name , font=("times new roman", 15)).place(x=150, y=210, width=200)
        self.ent_num = Entry(add_items_frame, textvariable=self.var_num, bd=2, font=("times new roman", 15))
        self.ent_buy = Entry(add_items_frame, textvariable=self.var_buy, bd=2, font=("times new roman", 15))
        self.ent_sell = Entry(add_items_frame, textvariable=self.var_sell, bd=2, font=("times new roman", 15))
        self.ent_groups = Entry(add_items_frame, textvariable=self.var_group, bd=2 ,font=("times new roman", 15))
        self.combo_fill1 =ttk.Combobox(add_items_frame, textvariable=self.var_fil1,values=self.fetch_data_from_db(), state='readonly', justify=CENTER, font=("times new roman", 15))
        self.combo_fill2 =ttk.Combobox(add_items_frame, textvariable=self.var_fil2,values=self.fetch_data_from_db(), state='readonly', justify=CENTER, font=("times new roman", 15))

       

       #label [المعبئة]
        self.lbl_fil1 = Label(add_items_frame, text="تعبئة 1 ", font=("times new roman", 18), bg="white")
        self.lbl_fil2 = Label(add_items_frame, text="تعبئة 2", font=("times new roman", 18), bg="white")
        self.lbl_numitem = Label(add_items_frame, text="عدد الطول", font=("times new roman", 18), bg="white")
        self.lbl_buyitem = Label(add_items_frame, text="شراء الطول", font=("times new roman", 18), bg="white")
        self.lbl_sellitem = Label(add_items_frame, text="بيع الطول ", font=("times new roman", 18), bg="white")
        self.lbl_num2item = Label(add_items_frame, text="عدد الطول", font=("times new roman", 18), bg="white")
        self.lbl_buy2item = Label(add_items_frame, text="شراء الطول", font=("times new roman", 18), bg="white")
        self.lbl_sell2item = Label(add_items_frame, text="بيع الطول ", font=("times new roman", 18), bg="white")
        
        
        #column 2


        # Setup Combobox

        data_from_db = self.fetch_data_from_db()
        
        # Initialize mycombo
        self.lbl_category = Label(add_items_frame, text="المجموعة", font=("times new roman", 18), bg="white").place(x=400, y=60)
        self.mycombo = ttk.Combobox(add_items_frame, values=data_from_db, justify=CENTER, state='readonly', font=("times new roman", 15))
        self.mycombo.place(x=150, y=60, width=200)

        # Set the current index only if there are values
        if data_from_db:
            self.mycombo.current(0)  # Set to the first item if available
        else:
            self.mycombo.set("No items available")  # Optionally set a default message


        print("Data from database:", data_from_db)  # Print fetched data to verify




       
        


    

        # Create a Spinbox
        self.spinbox = Spinbox(add_items_frame ,from_=0, to=100, increment=1.00, format="%.2f" , textvariable=self.var_spinebox , bd=2 , font=("times new roman", 15))
        



        txt_sup = Entry(add_items_frame, textvariable=self.var_sup, bd=2, font=("times new roman", 15)).place(x=150, y=110, width=200)

        
        cmb_fill = ttk.Combobox(add_items_frame, textvariable=self.var_itemtype, values=("اختار", "اعتيادية", "معبئة"), state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_fill.place(x=150, y=160, width=200)
        cmb_fill.current(0)
        cmb_fill.bind("<<ComboboxSelected>>", self.update_labels)

       
        
        #entries2 [التعبئة]
        self.ent_num2 = Entry(add_items_frame, textvariable=self.var_num2, bd=2, font=("times new roman", 15))
        self.ent_buy2 = Entry(add_items_frame, textvariable=self.var_buy, bd=2, font=("times new roman", 15))
        self.ent_sell2 = Entry(add_items_frame, textvariable=self.var_sell2item, bd=2, font=("times new roman", 15))
        

        def save_item():
            item_name =self.var_name.get()
            quantity_item = self.ent_num.get()
            buy_item = self.ent_buy.get()
            sell_item =self.ent_sell.get()
            group_item = self.ent_groups.get()

             # Ensure the item_name is provided
            if not item_name:
                messagebox.showwarning("Error", "اسم المادة مطلوب", parent=self.root)
                return
            
             # If other fields are empty, set them to None (NULL in SQLite)
            quantity_item = quantity_item if quantity_item else None
            buy_item = buy_item if buy_item else None
            sell_item = sell_item if sell_item else None
            group_item =  group_item if group_item else None

            


            
            if item_name:
                insert_items( item_name,quantity_item,sell_item,buy_item , group_item )
                messagebox.showinfo("Sucess", "تم اضافة التعبئة بنجاح", parent=self.root)
            
               
                
        add1_btn = Button(add_items_frame , text="sssssssاضافة", cursor="hand2", command=save_item, font=("times new roman", 25, "bold"), bg='#1E2A5E', fg="white")
        add1_btn.place(x=150,y=460, width=20)        

                

           
           
        
    
           
        
    def fetch_data_from_db(self):
        # Connect to SQLite database
        conn = sqlite3.connect('items.db')
        curr = conn.cursor()
        # Fetch data 
        curr.execute("SELECT group_name FROM groups") 
        data = curr.fetchall()
        # Extract data 
        data = [group[0] for group in data]
        # Close the connection
        conn.close()
        return data
        
        

        

    

        

       
        
        
    def update_labels(self, event):
        selected_value = self.var_itemtype.get()


        #label [الاعتيادي]
        self.lbl_num.place_forget()
        self.lbl_buy.place_forget()
        self.lbl_sell.place_forget()
        self.lbl_groups.place_forget()
        #entry [الاعتيادي]
        self.ent_num.place_forget()
        self.ent_buy.place_forget()
        self.ent_sell.place_forget()
        self.ent_groups.place_forget()




         #label [المعبئة]
        self.lbl_fil1.place_forget()
        self.lbl_fil2.place_forget()
        self.lbl_numitem.place_forget()
        self.lbl_buyitem.place_forget()
        self.lbl_sellitem.place_forget()
        self.lbl_num2item.place_forget()
        self.lbl_buy2item.place_forget()
        self.lbl_sell2item.place_forget()
         #entry [المعبئة]
        self.combo_fill1.place_forget()
        self.combo_fill2.place_forget()
        self.ent_sell2.place_forget()
        self.ent_num2.place_forget()
        self.ent_buy2.place_forget()
        self.spinbox.place_forget()

        if selected_value == "معبئة":

            self.lbl_fil1.place(x=390, y=310)
            self.lbl_fil2.place(x=110, y=310)
            self.lbl_numitem.place(x=400, y=360)
            self.lbl_buyitem.place(x=390, y=410)
            self.lbl_sellitem.place(x=400, y=460)
            self.lbl_num2item.place(x=150, y=360)
            self.lbl_buy2item.place(x=150, y=410)
            self.lbl_sell2item.place(x=150, y=460)
            self.combo_fill1.place(x=300, y=310, width=80)
            if self.combo_fill1['values']:  # Check if combo_fill1 has values
                self.combo_fill1.current(0)
        
            if self.combo_fill2['values']:  # Check if combo_fill2 has values
                self.combo_fill2.current(0)
            
            self.combo_fill2.place(x=20, y=310, width=80)
            self.ent_num.place(x=285, y=360, width=100)
            self.ent_buy.place(x=285, y=415, width=100)
            self.ent_sell.place(x=285, y=460, width=100)
            self.ent_num2.place(x=20, y=360, width=100)
            self.ent_buy2.place(x=20, y=415, width=100)
            self.ent_sell2.place(x=20, y=460, width=100)
            self.spinbox.place( x=180, y=310, width=80)
        else:
            
            self.lbl_num.place(x=420, y=260)
            self.lbl_buy.place(x=390, y=310)
            self.lbl_sell.place(x=400, y=360)
            self.ent_num.place(x=150,  y=260, width=200)
            self.ent_buy.place(x=150,y=310, width=200)
            self.ent_sell.place(x=150,y=360, width=200)
            self.lbl_groups.place( x =400 , y =400 )
            self.ent_groups.place(  x=150 , y= 400 )

           
            


if __name__ == "__main__":
    root = Tk()
    items = add_items(root)
    root.mainloop()