from tkinter import *
from PIL import Image, ImageTk
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700")
        self.root.title("الناهي للمبيعات")

        #title
        self.icon_title=PhotoImage(file="images\logo1.png")
        title=Label(self.root,text="الناهي للمبيعات", image=self.icon_title, compound=LEFT, font=("times new roman", 20, 'bold'),fg="blue",anchor="w", padx=20).place(x=1100, y=0, relwidth=1, height=70)


        btn_logout=Button(self.root,text="Logout",cursor="hand2", font=("arial", 15, 'bold'),bg='red').place(x=0,y=10,height=50,width=150)
# Initialize the main window
root=Tk()
obj=IMS(root)
root.mainloop()