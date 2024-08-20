from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("الناهي للمبيعات")
        self.root.config(bg="white")

        #title
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="الناهي للمبيعات", image=self.icon_title, compound=LEFT, font=("times new roman", 20, 'bold'),fg="blue",anchor="w", padx=20).place(x=1450, y=0, relwidth=5, height=70)

        #locgout
        btn_logout=Button(self.root,text="Logout",cursor="hand2", font=("arial", 20 , 'bold'),bg='red').place(x=0,y=10,height=50,width=150)

        #clock 
        self.lbl_clock=Label(self.root, text="Welcome to your Inventory Managment & Sales System \t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("arial", 15), bg="#4d636d",fg="white", anchor='w',padx=20)
        self.lbl_clock.place(x=0,y=70,relwidth=100,height=30)

        #right Menu
        self.menulogo=Image.open("images/menu_im.png")
        self.menulogo=self.menulogo.resize((200,200))
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        RightMenu=Frame(self.root,bd=2,borderwidth=2,height=50,relief=RIDGE,bg="white")
        RightMenu.place(x=1505,y=100,width=200,height=1920)

        lbl_menulogo=Label(RightMenu, image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")

        self.icon_menu=Image.open("images/options.png")
        self.icon_menu=self.icon_menu.resize((40,30))
        self.icon_menu=ImageTk.PhotoImage(self.icon_menu)
        
        btn_menu=Button(RightMenu, image=self.icon_menu, compound=LEFT).pack(side=TOP,fill=X)
        btn_storage=Button(RightMenu,text="المخزن",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_sale=Button(RightMenu,text="بيع",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_buy=Button(RightMenu,text="شراء",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_bonds=Button(RightMenu,text="السندات",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_account=Button(RightMenu,text="الحسابات",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_acoountreports=Button(RightMenu,text="تقارير الحسابات",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_inovicereports=Button(RightMenu,text="تقارير القوائم",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_revenuereports=Button(RightMenu,text="تقارير الارباح",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_materialsreports=Button(RightMenu,text="تقارير المواد",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_users=Button(RightMenu,text="المستخدمين",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        btn_tools=Button(RightMenu,text="الادوات",image=self.icon_side,compound=LEFT,padx=5,cursor="hand2", font=("arial", 15, "bold" ),bg='white',bd=3).pack(side=TOP,fill=X)
        
        #left frame
        Leftframe=Frame(self.root,borderwidth=2,height=1920 , width=1080 ,relief=RIDGE,bg="#1E2A5E")
        Leftframe.place(x=0,y=100,width=1504,height=1920)

        #fast reach
        self.fastreach=Label(self.root, text="الوصول السريع",fg="white",bg='#1E2A5E', font=("times new roman", 20)).place(x=1300, y=180)
        self.lbl_storage = Label(self.root, text="المخزن\nالمواد", fg='black', bg='white', font=("times new roman", 20))
        self.lbl_storage.place(x=1275, y=250,height=180, width=180)
        self.lbl_sale = Label(self.root, text="قائمة بيع", fg='black', bg='white', font=("times new roman", 20))
        self.lbl_sale.place(x=1075, y=250,height=180, width=180)
        self.lbl_buy = Label(self.root, text="قائمة شراء", fg='black', bg='white', font=("times new roman", 20))
        self.lbl_buy.place(x=875, y=250,height=180, width=180)
        self.lbl_recievebonds = Label(self.root, text="سند قبض", fg='black', bg='white', font=("times new roman", 20))
        self.lbl_recievebonds.place(x=675, y=250,height=180, width=180)

        #Line of fast reach
        self.line=Frame(self.root, borderwidth=1, height=1000, width=10, relief=RIDGE, bg='white')
        self.line.place(x=1295, y=220, width=150, height=3)


        #bottom label
        lbl_bottom=Label(self.root, text="Inventory Managment System || Developed by Ali Alnahi & Ameer Mazin\nContact:alialhaqjasim@gmail.com for any isuues",font=("arial", 15), bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        


# Initialize the main window
root=Tk()
myapp=App(root)
root.mainloop()