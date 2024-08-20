from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from category import categoryClass
from storage import add_items

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("الناهي للمبيعات")
        self.root.config(bg="white")

        # title
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="الناهي للمبيعات", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 20, 'bold'), fg="blue", anchor="w", padx=20)
        title.place(x=1650, y=0, relwidth=5, height=70)

        # logout
        btn_logout = Button(self.root, text="Logout", cursor="hand2", font=("times new roman", 20, 'bold'), bg='red')
        btn_logout.place(x=0, y=10, height=50, width=150)

        # clock
        self.lbl_clock = Label(self.root, text="Welcome to your Inventory Management & Sales System \t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white", anchor='w', padx=20)
        self.lbl_clock.place(x=0, y=70, relwidth=100, height=30)

        # right Menu
        self.menulogo = Image.open("images/menu_im.png")
        self.menulogo = self.menulogo.resize((200, 200))
        self.menulogo = ImageTk.PhotoImage(self.menulogo)

        RightMenu = Frame(self.root, bd=2, borderwidth=2, height=50, relief=RIDGE, bg="white")
        RightMenu.place(x=1720, y=100, width=200, height=1920)

        lbl_menulogo = Label(RightMenu, image=self.menulogo)
        lbl_menulogo.pack(side=TOP, fill=X)

        self.icon_side = PhotoImage(file="images/side.png")

        self.icon_menu = Image.open("images/options.png")
        self.icon_menu = self.icon_menu.resize((40, 30))
        self.icon_menu = ImageTk.PhotoImage(self.icon_menu)

        btn_menu = Button(RightMenu, image=self.icon_menu, compound=LEFT, command=self.toggle_menu_buttons)
        btn_menu.pack(side=TOP, fill=X)

        # Create the buttons
        self.storage_dropdown_frame = None #frame to hold the dropdown list
        self.btn_storage = Button(RightMenu, text="المخزن", image=self.icon_side, compound=LEFT,command=self.toggle_storage_dropdown, padx=5, cursor="hand2", 
                                 font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_sale = Button(RightMenu, text="بيع", image=self.icon_side, compound=LEFT, padx=5, cursor="hand2", 
                               font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_buy = Button(RightMenu, text="شراء", image=self.icon_side, compound=LEFT, padx=5, cursor="hand2", 
                              font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_bonds = Button(RightMenu, text="السندات", image=self.icon_side, compound=LEFT, padx=5, cursor="hand2", 
                                font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_account = Button(RightMenu, text="الحسابات", image=self.icon_side, compound=LEFT, padx=5, cursor="hand2", 
                                  font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_acoountreports = Button(RightMenu, text="تقارير الحسابات", image=self.icon_side, compound=LEFT, padx=5, 
                                         cursor="hand2", font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_inovicereports = Button(RightMenu, text="تقارير القوائم", image=self.icon_side, compound=LEFT, padx=5, 
                                         cursor="hand2", font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_revenuereports = Button(RightMenu, text="تقارير الارباح", image=self.icon_side, compound=LEFT, padx=5, 
                                         cursor="hand2", font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_materialsreports = Button(RightMenu, text="تقارير المواد", image=self.icon_side, compound=LEFT, padx=5, 
                                           cursor="hand2", font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_users = Button(RightMenu, text="المستخدمين", image=self.icon_side, compound=LEFT, padx=5, cursor="hand2", 
                                font=("times new roman", 15, "bold"), bg='white', bd=3)
        self.btn_tools = Button(RightMenu, text="الادوات", image=self.icon_side, compound=LEFT, padx=5, cursor="hand2", 
                                font=("times new roman", 15, "bold"), bg='white', bd=3)

        # Add the buttons to the list and pack them
        self.menu_buttons = [self.btn_storage, self.btn_sale, self.btn_buy, self.btn_bonds, self.btn_account, self.btn_acoountreports, 
                             self.btn_inovicereports, self.btn_revenuereports, self.btn_materialsreports, self.btn_users, self.btn_tools]
        for btn in self.menu_buttons:
            btn.pack(side=TOP, fill=X)

    
        # left frame
        Leftframe = Frame(self.root, borderwidth=2, height=1920, width=1080, relief=RIDGE, bg="#1E2A5E")
        Leftframe.place(x=0, y=100, width=1724, height=1920)

        # fast reach
        self.fastreach = Label(self.root, text="الوصول السريع", fg="white", bg='#1E2A5E', font=("times new roman", 20)).place(x=1300, y=180)
        self.lbl_storage = Label(self.root, text="المخزن\nالمواد", fg='black', bg='white', font=("times new roman", 20))
        self.lbl_storage.place(x=1275, y=250, height=180, width=180)
        self.lbl_sale = Label(self.root, text="قائمة بيع", fg='black', bg='white', font=("times new roman", 20))
        self.lbl_sale.place(x=1075, y=250, height=180, width=180)
        self.lbl_buy = Label(self.root, text="قائمة شراء", fg='black', bg='white', font=("times new roman", 20))
        self.lbl_buy.place(x=875, y=250, height=180, width=180)
        self.lbl_recievebonds = Label(self.root, text="سند قبض", fg='black', bg='white', font=("times new roman", 20))
        self.lbl_recievebonds.place(x=675, y=250, height=180, width=180)

        # Line of fast reach
        self.line = Frame(self.root, borderwidth=1, height=1000, width=10, relief=RIDGE, bg='white')
        self.line.place(x=1295, y=220, width=150, height=3)

        # bottom label
        lbl_bottom = Label(self.root, text="Inventory Management System || Developed by Ali Alnahi & Ameer Mazin\nContact:alialhaqjasim@gmail.com for any issues", 
                           font=("times new roman", 15), bg="#4d636d", fg="white")
        lbl_bottom.pack(side=BOTTOM, fill=X)

    def toggle_menu_buttons(self):
        if self.btn_storage.winfo_viewable():
            for btn in self.menu_buttons:
                btn.pack_forget()  # Hide the buttons
        else:
            for btn in self.menu_buttons:
                btn.pack(side=TOP, fill=X)  # Show the buttons again

    def toggle_storage_dropdown(self):
        if self.storage_dropdown_frame: 
            self.storage_dropdown_frame.destroy()
            self.storage_dropdown_frame = None  #hide the list
        else:
            self.storage_dropdown_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white") #show the list
            self.storage_dropdown_frame.place(x=1520, y=300, width=200, height=150)
            btn_material = Button(self.storage_dropdown_frame, text="المواد", cursor="hand2", command=self.new_items_add, font=("times new roman", 12, "bold"), bg='white').pack(side=TOP, fill=X)
            btn_fills = Button(self.storage_dropdown_frame, text="التعبئات", cursor="hand2", font=("times new roman", 12, "bold"), bg='white').pack(side=TOP, fill=X)
            btn_parcodeprint = Button(self.storage_dropdown_frame, text="طباعة باركود", cursor="hand2", font=("times new roman", 12, "bold"), bg='white').pack(side=TOP, fill=X)
            btn_category = Button(self.storage_dropdown_frame, text="المجموعات", cursor="hand2", font=("times new roman", 12, "bold"), bg='white').pack(side=TOP, fill=X)
    def new_items_add(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = add_items(self.new_win)
# Initialize the main window
if __name__ == "__main__":
    root = Tk()
    myapp = App(root)
    root.mainloop()
