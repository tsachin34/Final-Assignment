import sys
import os

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from ttkthemes import themed_tk as tk
from tkinter import messagebox 
# from tkcalendar import DateEntry
import rentCar
import userParking

# from ..Classes.userData import User
sys.path.append("D:/Second Semester/Algorithm/Assignment Drafts/Classes")
from userData import *
from Orders import *

class userInterface:
    """ This class is made to buid a proper Login System"""
    def __init__(self,user):
        """This is an intialization method to add attributes"""
        self.wn=Tk()
        self.wn.title("Menu")
        self.wn.geometry("430x580+300+100")
        self.wn.configure(background="#3198F5")

        self.user=user
        self.order=Order()

        

     
        self.topLevel=Label(self.wn,text="Welcome  " + self.user[1]  ,fg="white",bg="#015AAA",font=("Calibri",16,"bold"))
        self.topLevel.place(x=0,y=0,relwidth=1)

        self.frame1=Frame(self.wn)
        self.frame1.place(x=100,y=50)
        self.frame1.configure(background="#3198F5")

        
        self.rent_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/python/Online/finalAssignment/images/rental.png").resize((60,65)))
        self.rent_label=Label(self.frame1,image=self.rent_image,background="#3198F5")
        self.rent_label.grid(row=0,column=0)


        self.btn1 = Button(self.frame1, text='Rent A Car', font=('Calibri', 16,"bold"), fg="white",background='#3198F5',width=20, bd=1,command=self.onRentClick)
        self.btn1.grid(row=1,column=0,pady=10)

        self.park_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/python/Online/finalAssignment/images/parking2.png").resize((60,65)))
        self.park_label=Label(self.frame1,image=self.park_image,background="#3198F5")
        self.park_label.grid(row=2,column=0)

        self.btn2 = Button(self.frame1, text='Book parking spot', font=('Calibri', 16,"bold"), fg="white",background='#3198F5',width=20, bd=1,command=self.bookParkingSpot)
        self.btn2.grid(row=3,column=0,pady=10)

        self.cancel_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/python/Online/finalAssignment/images/cancelcar.png").resize((60,65)))
        self.cancel_label=Label(self.frame1,image=self.cancel_image,background="#3198F5")
        self.cancel_label.grid(row=4,column=0)

        self.btn3 = Button(self.frame1, text='Transaction History', font=('Calibri', 16,"bold"), fg="white",background='#3198F5',width=20, bd=1, command= self.transactionHistory)
        self.btn3.grid(row=5,column=0,pady=10)

        self.contact_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/python/Online/finalAssignment/images/contact.png").resize((50,55)))
        self.contact_label=Label(self.frame1,image=self.contact_image,background="#3198F5")
        self.contact_label.grid(row=6,column=0)

        self.btn4 = Button(self.frame1, text="Contact Us", font=('Calibri', 16,"bold"), fg="white",background='#3198F5',width=20, bd=1,command=self.contact)
        self.btn4.grid(row=7,column=0,pady=10)


        self.wn.mainloop()

    def contact(self):
        messagebox.showinfo("Contact Details","Phone: 9862146970\nEmail: KJkjkj@gmail.com")
        # print(self.user)
    
    def onRentClick(self):
        self.wn.destroy()
        self.rent=rentCar.placeOrder(self.user)
        
        # logged=Toplevel(self.wn)
        # rentCar.placeOrder(logged)
    def bookParkingSpot(self):
        self.wn.destroy()
       
        park=userParking.Parking(self.user)

    
    def transactionHistory(self):
        self.wn.destroy()
        user= self.user
        # data=self.order.showOrder(user)
        # messagebox.showinfo("History",data)
       
        iv=Transaction(user)

class Transaction:
    def __init__(self, user):
        """This is an intialization method to add attributes"""
        self.wn=tk.ThemedTk()
        # self.wn=Tk()
        self.wn.configure(bg="#6262ED")
        self.wn.title("User")
        self.wn.geometry("530x270+200+50")

        self.wn.get_themes()
        # self.s = ttk.Style(self.wn)
        self.wn.set_theme('plastik')

        self.user=user
        self.order=Order()
        # data=self.order.showOrder(self.user)
        # messagebox.showinfo("History",data)


        self.frame1=Frame(self.wn,bd=5)
        self.frame1.place(x=20,y=10)
        self.frame1.configure(background="#6262ED")

        self.orders_tree = ttk.Treeview(self.frame1, columns=( 'brand','model', 'pickUpDate','location','days','price'))
        self.orders_tree.grid(row=0, column=0)
        self.orders_tree['show'] = 'headings'
        # self.orders_tree.column('username', width=90, anchor='center')
        self.orders_tree.column('brand', width=90, anchor='center')
        self.orders_tree.column('model', width=90, anchor='center')        
        self.orders_tree.column('pickUpDate', width=100, anchor='center')
        self.orders_tree.column('location', width=90, anchor='center')
        self.orders_tree.column('days', width=50, anchor='center')
        self.orders_tree.column('price', width=50, anchor='center')
        self.orders_tree.heading('brand', text="Brand")
        # self.orders_tree.heading('username', text="Username")
        self.orders_tree.heading('days', text="Days")
        self.orders_tree.heading('pickUpDate', text="Pick Up")
        self.orders_tree.heading('model', text="Model")
        self.orders_tree.heading('price', text="Price")
        self.orders_tree.heading('location', text="Address")

        self.showHistory()

        self.show_menu()


    



        
         


        self.wn.get_themes()
        # self.s = ttk.Style(self.wn)
        self.wn.set_theme('plastik')


    def showHistory(self):
        self.orders_tree.delete(*self.orders_tree.get_children())
        data=self.order.showOrder(self.user[1])
        for i in data:
            self.orders_tree.insert("", "end",text=i[0] , value=(i[2], i[3],i[4],i[5],i[6],i[7]))
    
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_cascade(label="Return",command=self.mainMenu)
        file_menu.add_cascade(label="Exit",command=self.exitWn)
    
    def mainMenu(self):
        self.wn.destroy()
        iv=userInterface(self.user)

    def exitWn(self):
        ans=messagebox.askquestion("Exit","Are you sure?")
        if ans=="yes":
            self.wn.destroy()
        
       



# v=Transaction()
# iv=userInterface()