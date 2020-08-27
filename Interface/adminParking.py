import sys

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from ttkthemes import themed_tk as tk

sys.path.append("D:/Second Semester/Algorithm/Assignment Draft/Classes")
import Admn
import adminWn
from userData import *
from parking import *


class parkDetails:
    def __init__(self):
        self.wn=tk.ThemedTk()
        # self.wn=Tk()
        self.wn.configure(bg="#6262ED")
        self.wn.title("Parking Details")
        self.wn.geometry("620x480+200+100")

        self.park=Park()
        self.item_index = ""
        self.my_index = 1

        self.frame1=Frame(self.wn,bg="#6262ED")
        self.frame1.place(x=10,y=30)

        self.lb_spot= Label(self.frame1,font=("Calibri",14,"bold"),text="Spot no:",bg="#6262ED",fg="black")
        self.lb_spot.grid(row=0,column=0)

        self.ent_spot=Entry(self.frame1,font=("Calibri",12),width=7)
        self.ent_spot.grid(row=0,column=1)

        self.btn_add=Button(self.frame1, text='Add', font=('Calibri', 11,"bold"), fg="white",background='#6262ED',width=12, bd=1,command=self.add_park)
        self.btn_add.grid(row=0,column=2,padx=10)

        self.frame2=Frame(self.wn,bg="#6262ED")
        self.frame2.place(x=10,y=100)

        self.details_tree = ttk.Treeview(self.frame2, columns=('Username','Brand', 'Model','Vechile Type', 'Spot','booking time'))
        self.details_tree.grid(row=0,column=0)
        self.details_tree['show'] = 'headings'
        self.details_tree.column('Username', width=100, anchor='center')
        self.details_tree.column('Brand', width=100, anchor='center')
        self.details_tree.column('Model', width=100, anchor='center')
        self.details_tree.column('Vechile Type', width=120, anchor='center')        
        self.details_tree.column('Spot', width=60, anchor='center')
        self.details_tree.column('booking time', width=100, anchor='center')
        self.details_tree.heading('Username', text="Username")
        self.details_tree.heading('Brand', text="Brand")
        self.details_tree.heading('Model', text="Model")
        self.details_tree.heading('Vechile Type', text="Vechile Type")
        self.details_tree.heading('Spot', text="Spot")
        self.details_tree.heading('booking time', text="Booking Time")


        self.delete_button=Button(self.wn, text="Delete", font=('Calibri', 11,"bold"), fg="white",background='#C31616',width=15, bd=1,command=self.deleteBooking)
        self.delete_button.place(x=10,y=390)

        self.details_tree.bind("<Double-1>", self.select_item)


        self.show_menu()
        self.showDetails()

        self.wn.mainloop()
    
    def add_park(self):
        spot=self.ent_spot.get()
        if self.park.add_spot(spot):
            messagebox.showinfo("Sucessfull","Parking spot added")
        else:
            messagebox.showerror("Error","Sorry something went wrong")

    def showDetails(self):
        self.details_tree.delete(*self.details_tree.get_children())
        data=self.park.showData()
        for i in data:
            self.details_tree.insert("", "end",text=i[0] , value=(i[1], i[2],i[3],i[4],i[5],i[6]))

    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_cascade(label="Return",command=self.mainMenu)
        file_menu.add_cascade(label="Exit")

    def select_item(self, event):
        selected_item = self.details_tree.selection()[0]
        self.item_index = self.details_tree.item(selected_item, 'text')
        print(self.item_index)

    def deleteBooking(self):
        index=self.item_index
        ans=messagebox.askquestion("Delete","Are you sure?")
        if ans=="yes":
            if self.park.delete_booking(index):
                messagebox.showinfo("Sucess", "Item deleted")
                self.showDetails()
            else:
                messagebox.showerror("Error", "Item cannot be deleted")

    def mainMenu(self):
        self.wn.destroy()
        # self.admin=adminWn.Cars()



    
    

        

# iv=parkDetails()