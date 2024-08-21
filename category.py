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

        #update the listbox
        def update(data):
            #clear the listbox
            my_listbox.delete(0 , END)

            #add my list to listbox
            for item in data:
                my_listbox.insert(END , item)

        #update entry box with listbox cliked
        def fillout(e):
            #delete anything in the entry box
            my_entry.delete(0, END)

            #add cliked list item to entry box 
            my_entry.insert(0, my_listbox.get(my_listbox.curselection()))


        #create func to check entry vs listbox
        def check(e):
            #grap what was typed
            typed = my_entry.get()

            if typed == '':
                data =my_list
            else:
                data = []
            for item in my_list:
                if typed.lower() in item.lower():
                    data.append(item)

            update(data)





        

         #create a label
        my_label= Label(root , text="start typing..." , font=("helvetica" , 14) , fg="grey")
        my_label.pack(pady=20)

        #creat entry box
        my_entry = Entry(root , font=("helvetica" , 20))
        my_entry.pack()
        
        #listbox
        my_listbox = Listbox(root , width=50)
        my_listbox.pack(pady=15)
        #add item to listbox
        my_listbox.insert(END, "item1" )
        my_listbox.insert(END, "item2")
        #add item to list
        my_list = ["one" , "onlyone" ,  "two" , "three" , "tree"  , ]
        for item in my_list:
            my_listbox.insert(0, item)
        update(my_list)


        my_listbox.bind(" <<ListboxSelect>>" , fillout)

        my_entry.bind("<KeyRelease>" , check)