import sys

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from ttkthemes import themed_tk as tk
from tkinter import messagebox 

import time
import rentCar
import userMenu

sys.path.append("D:/Second Semester/Algorithm/Assignment Draft/Classes")
from userData import *
from parking import *


class Parking:
    """The class is constructed to make a parking system that can be accessed by the user"""
    def __init__(self,user):
        self.wn=tk.ThemedTk()
        self.wn.configure(bg="#6262ED")
        self.wn.title("Park your vechile")
        self.wn.geometry("620x480+200+100")

        self.park=Park()
        self.user=user

        self.frame1=Frame(self.wn,bg="#6262ED")
        self.frame1.place(x=10,y=30)

        self.inframe=Frame(self.wn,bg="#6262ED")
        self.inframe.place(x=290,y=30)

        
        self.lb_cbrand= Label(self.frame1,font=("Calibri",14,"bold"),text="Brand:",bg="#6262ED",fg="#060347")
        self.lb_cbrand.grid(row=0,column=0)

        self.ent_cbrand=Entry(self.frame1,font=("Verdana",10))
        self.ent_cbrand.grid(row=0,column=1)

        self.lb_cmodel= Label(self.frame1,font=("Calibri",14,"bold"),text="Model:",bg="#6262ED",fg="#060347")
        self.lb_cmodel.grid(row=1,column=0)

        self.ent_cmodel=Entry(self.frame1,font=("Verdana",10))
        self.ent_cmodel.grid(row=1,column=1,padx=5)

        self.lb_type= Label(self.inframe,font=("Calibri",14,"bold"),text="Vechile type:",bg="#6262ED",fg="#060347")
        self.lb_type.grid(row=0,column=2)

        self.lb_spot=Label(self.inframe,font=("Calibri",14,"bold"),text="Parking spot:",bg="#6262ED",fg="#060347")
        self.lb_spot.grid(row=1,column=2)

        self.combo_type = ttk.Combobox(self.inframe, state='enabled',width=15,font=("Verdana",10))
        self.combo_type.grid(row=0, column=3)
        self.combo_type['values'] = ["Moterbike","SUV","Pickup","Minivan","Roadster","Wagon","Taxi"]

        self.combo_spot= ttk.Combobox(self.inframe, state='readonly',width=15,font=("Verdana",10))
        self.combo_spot.grid(row=1, column=3)
        self.combo_spot['values'] = self.park.avilable_spots()

        self.park_button=Button(self.wn, text="Park", font=('Calibri', 11,"bold"), fg="white",background='#6262ED',width=25, bd=1,command=self.bookSpot)
        self.park_button.place(x=160,y=100)

        self.message_frame=LabelFrame(self.wn,bd=10,padx=10,relief=RIDGE,font=("Calibri",12,"bold"),text="Message Box",bg="#6262ED")
        self.message_frame.place(x=10,y=170,width=600,height=250)

        self.message1= Label(self.message_frame,font=("Calibri",14,"bold"),text="    Please enter your vechile detalis before booking a spot.",bg="#6262ED",fg="#060347")
        self.message1.grid(row=1,column=0)



        self.show_menu()
        self.message()

        
        

        self.wn.mainloop()

    


    def bookSpot(self):
        brand= self.ent_cbrand.get()
        model = self.ent_cmodel.get()
        type= self.combo_type.get()
        spot= self.combo_spot.get()
        user=self.user[1]

        if self.validate():
            t = time.localtime()
            current_time = time.strftime("%H:%M", t)
            if self.park.confirm_parking(user,brand,model,type,spot,current_time):
                messagebox.showinfo("Booked", "Spot booked, you can park now")
                self.combo_spot.set('')
                self.combo_spot['values'] = self.park.avilable_spots()
                self.message()
            else:
                messagebox.showerror("Error", "Something went wrong")




    
    def validate(self):
        brand= self.ent_cbrand.get()
        model = self.ent_cmodel.get()
        type= self.combo_type.get()
        spot= self.combo_spot.get()


        if brand=='' or model=='' or type=='' or spot=='':
            messagebox.showerror("Error", "Dont leave Entry field Empty")
            return False

        else:
            return True

    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_cascade(label="Rent car",command=self.openRentTab)
        file_menu.add_cascade(label="History",command=self.openHistory)
        file_menu.add_cascade(label="Log Out")

    def openRentTab(self):
        self.wn.destroy()
        iv=rentCar.placeOrder(self.user)

    def openHistory(self):
        user= self.user
        self.wn.destroy()
        iv=userMenu.Transaction(user)


    def message(self):
        """This function shows the status of parking spot"""       
        if self.park.spotUnavilable():
            self.message2= Label(self.message_frame,font=("Calibri",14,"bold"),
            text= "     No parking spot available currently, Please try again later. ",bg="#6262ED",fg="#AB0610")
            self.message2.grid(row=1,column=0)
        else:
            spots=len(self.park.avilable_spots())
            self.message2= Label(self.message_frame,font=("Calibri",14,"bold")
            ,text= f"There are {spots} spots available currently" ,bg="#6262ED",fg="#060347")
            self.message2.grid(row=2,column=0)






# iv=Parking()