from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
class fillsClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x750+220+130")
        self.root.title("الناهي للمبيعات")
        self.root.config(bg="white")
        self.root.focus_force()

        
        srch_lbl = Label(self.root, text="البحث",bg= "white", fg='#1E2A5E', font=("arial", 20 )).place(x=900, y=40)
        srch_bar = Entry(self.root, bd=2, bg="white", fg="#1E2A5E", justify=CENTER, relief=RIDGE, font=("arial", 18))
        srch_bar.place(x=350, y=40, width=500)
        
        fills_frame = Frame(self.root, bd=2, bg="white", borderwidth=2, relief=RIDGE, )
        fills_frame.place(x=350, y=120, width=500, height=500)
        fills_lbl = Label(self.root, text="اسم التعبئة", fg='#1E2A5E', font=("arial", 20 )).place(x=350, y=100, width=500, height=30)

        add_btn = Button(self.root, text="اضافة", cursor="hand2",command=self.add_cat, font=("times new roman", 15, "bold"), bg='#1E2A5E', fg="white")
        add_btn.place(x=750, y=630, width=100, height=50)
        remove_btn = Button(self.root, text="حذف", cursor="hand2", font=("times new roman", 15, "bold"), bg='red', fg="white")
        remove_btn.place(x=630, y=630, width=100, height=50)

    

    def add_cat(self):
        self.new_win = Toplevel(self.root)
        self.new_win.geometry("600x600+500+130")
        self.new_win.title("اضافة تعبئات")
        self.new_obj = (self.new_win)

if __name__=="__main__":
    root=Tk()
    fil = fillsClass(root)
    root.mainloop()
