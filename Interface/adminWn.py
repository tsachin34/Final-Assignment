import sys

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from ttkthemes import themed_tk as tk

sys.path.append("D:/Second Semester/Algorithm/Assignment Draft/Classes")
import Admn
from userData import *
import adminParking

class Cars:
    """This class performs the fuction of main Admin window"""
    def __init__(self):
        self.wn=tk.ThemedTk()
        self.wn.configure(bg="#6262ED")
        self.wn.title("Car Rental and Parking System")
        self.wn.geometry("620x480+200+100")

        self.item_index = ""
        self.my_index = 1
        self.admin=Admn.Admin()
        self.user=User()

        self.wn.get_themes()
        self.wn.set_theme('scidblue')

        self.notebook = ttk.Notebook(self.wn)
        self.notebook.place(x = 0, y = 0, width = 650, height = 620)
        self.add_tab = Frame(self.notebook)
        self.orders_tab = Frame(self.notebook)
        self.user_tab = Frame(self.notebook)
        
        self.notebook.add( self.add_tab, text = 'Add Cars')
        self.notebook.add(self.orders_tab, text = 'View Orders')
        self.notebook.add(self.user_tab, text = 'Add User')
        
        self.add_tab.configure(bg="#6262ED")
        self.user_tab.configure(bg="#6262ED")
        self.orders_tab.configure(bg="#6262ED")

        #===============================Add_cars_tab==============================================================#
        self.frame1=Frame(self.add_tab,bg="#6262ED")
        self.frame1.place(x=10,y=30)

        self.inframe=Frame(self.add_tab,bg="#6262ED")
        self.inframe.place(x=290,y=30)

        
        self.lb_cbrand= Label(self.frame1,font=("Calibri",14,"bold"),text="Brand:",bg="#6262ED",fg="black")
        self.lb_cbrand.grid(row=0,column=0)

        self.ent_cbrand=Entry(self.frame1,font=("Verdana",10))
        self.ent_cbrand.grid(row=0,column=1)

        self.price_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/Assignment Draft/images/dollar.png").resize((25,25)))
        self.price_label=Label(self.inframe,image=self.price_image,background='#6262ED',fg="blue")
        self.price_label.grid(row=0,column=2)

        self.ent_cprice=Entry(self.inframe,font=("Verdana",10),width=17)
        self.ent_cprice.grid(row=0,column=3)


        self.lb_cmodel= Label(self.frame1,font=("Calibri",14,"bold"),text="Model:",bg="#6262ED",fg="black")
        self.lb_cmodel.grid(row=1,column=0)

        self.ent_cmodel=Entry(self.frame1,font=("Verdana",10))
        self.ent_cmodel.grid(row=1,column=1,padx=5)

        self.address_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/Assignment Draft/images/garage.png").resize((25,25)))
        self.address_label=Label(self.inframe,image=self.address_image,background='#6262ED',fg="blue")
        self.address_label.grid(row=1,column=2,padx=5)

        self.combo_address = ttk.Combobox(self.inframe, state='enabled',width=15,font=("Verdana",10))
        self.combo_address.grid(row=1, column=3)
        self.combo_address['values'] = ["Kathmandu","Pokhara","Butwal","Biratnagar","Hetauda","Dhulikhel","Kapilvastu"]

        self.add_button=Button(self.add_tab, text="Add", font=('Calibri', 11,"bold"), fg="white",background='#6262ED',width=15, bd=1,command=self.addCar)
        self.add_button.place(x=20,y=100)

        self.update_button=Button(self.add_tab, text="Update", font=('Calibri', 11,"bold"), fg="white",background='#6262ED',width=15, bd=1,command=self.update_cars)
        self.update_button.place(x=170,y=100)

        self.reset_button=Button(self.add_tab, text="Reset", font=('Calibri', 11,"bold"), fg="white",background='#6262ED',width=15, bd=1,command=self.reset)
        self.reset_button.place(x=320,y=100)

        self.frame2=Frame(self.add_tab,bg="#6262ED")
        self.frame2.place(x=10,y=150)

        self.cars_tree = ttk.Treeview(self.frame2, columns=('Brand', 'Model', 'Price','Address'))
        self.cars_tree.grid(row=1, column=0, columnspan=2)
        self.cars_tree['show'] = 'headings'
        self.cars_tree.column('Brand', width=200, anchor='center')
        self.cars_tree.column('Model', width=200, anchor='center')
        self.cars_tree.column('Price', width=100, anchor='center')        
        self.cars_tree.column('Address', width=100, anchor='center')
        self.cars_tree.heading('Brand', text="Brand")
        self.cars_tree.heading('Model', text="Model")
        self.cars_tree.heading('Price', text="Price")
        self.cars_tree.heading('Address', text="Avaiable Address")

        

        self.show_cars_tree()

        self.delete_button=Button(self.add_tab, text="Delete", font=('Calibri', 11,"bold"), fg="white",background='#C31616',width=15, bd=1,command=self.del_cars)
        self.delete_button.place(x=10,y=390)

        self.exit_button=Button(self.add_tab, text="Exit", font=('Calibri', 11,"bold"), fg="white",background='#C31616',width=15, bd=1, command= self.exitWn)
        self.exit_button.place(x=480,y=390)

        #===================================================Add_user_tab====================================================================#
        self.lb_head=Label(self.user_tab,text="User Registration",fg="White",font=("Calibri",20,"bold"),bg="#015AAA")
        self.lb_head.place(x=0,y=0,relwidth=1)

        self.frame3=Frame(self.user_tab,bd=20)
        self.frame3.place(x=50,y=50)
        
        self.frame3.configure(background="#6262ED")

        self.lb_usrname=Label(self.frame3,text="User Name:", fg="Black",font=("Calibri",14,"bold"),bg="#6262ED")
        self.lb_usrname.grid(row=0,column=0)

        self.lb_pw=Label(self.frame3,text="Password:", fg="Black",font=("Calibri",14,"bold"),bg="#6262ED")
        self.lb_pw.grid(row=1,column=0)

        self.lb_name=Label(self.frame3,text="Name:", fg="Black",font=("Calibri",14,"bold"),bg="#6262ED")
        self.lb_name.grid(row=2,column=0)

        self.lb_add=Label(self.frame3,text="Address:", fg="Black",font=("Calibri",14,"bold"),bg="#6262ED")
        self.lb_add.grid(row=3,column=0)

        self.lb_phone=Label(self.frame3,text="Phone:", fg="Black",font=("Calibri",14,"bold"),bg="#6262ED")
        self.lb_phone.grid(row=4,column=0)

        self.lb_email=Label(self.frame3,text="E-mail:", fg="Black",font=("Calibri",14,"bold"),bg="#6262ED")
        self.lb_email.grid(row=5,column=0)
        
        self.lb_type=Label(self.frame3,text="Type:", fg="Black",font=("Calibri",14,"bold"),bg="#6262ED")
        self.lb_type.grid(row=6,column=0)

        #====================================Entryyy=======================================================#
        self.ent_username=Entry(self.frame3,font=("arial",14))
        self.ent_username.grid(row=0,column=1,padx=10,pady=10)

        self.ent_pass=Entry(self.frame3,font=("arial",14,),show="*")
        self.ent_pass.grid(row=1,column=1,padx=10,pady=10)

        self.ent_name=Entry(self.frame3,font=("arial",14))
        self.ent_name.grid(row=2,column=1,padx=10,pady=10)
        
        self.ent_add=Entry(self.frame3,font=("arial",14,))
        self.ent_add.grid(row=3,column=1,padx=10,pady=10)

        self.ent_phone=Entry(self.frame3,font=("arial",14,))
        self.ent_phone.grid(row=4,column=1,padx=10,pady=10)

        self.ent_email=Entry(self.frame3,font=("arial",14))
        self.ent_email.grid(row=5,column=1,padx=10,pady=10)

        self.combo_type = ttk.Combobox(self.frame3, state='readonly',width=20)
        self.combo_type.grid(row=6, column=1)
        self.combo_type['values'] = ["User","Admin"]

        self.btn = Button(self.user_tab, text='Register',font=('Calibri', 11,"bold"), fg="white",background='#6262ED',width=12, bd=1, command=self.rgstr_btn)
        self.btn.place(x=300,y=410)
        
        self.btn3 = Button(self.user_tab, text='Reset', font=('Calibri', 11,"bold"), fg="white",background='#6262ED',width=12, bd=1, command=self.reset_val)
        self.btn3.place(x=410,y=410)

        self.show_menu()

        #===========================================view orders tab=================================================#
        self.frame4=Frame(self.orders_tab,bd=5)
        self.frame4.place(x=0,y=0)
        self.frame4.configure(background="#6262ED")

        self.orders_tree = ttk.Treeview(self.frame4, columns=('username', 'brand','model', 'pickUpDate','location','days','price'), height=15)
        self.orders_tree.grid(row=0, column=0)
        self.orders_tree['show'] = 'headings'
        self.orders_tree.column('username', width=90, anchor='center')
        self.orders_tree.column('brand', width=90, anchor='center')
        self.orders_tree.column('model', width=90, anchor='center')        
        self.orders_tree.column('pickUpDate', width=100, anchor='center')
        self.orders_tree.column('location', width=90, anchor='center')
        self.orders_tree.column('days', width=50, anchor='center')
        self.orders_tree.column('price', width=95, anchor='center')
        self.orders_tree.heading('brand', text="Brand")
        self.orders_tree.heading('username', text="Username")
        self.orders_tree.heading('days', text="Days")
        self.orders_tree.heading('pickUpDate', text="Pick Up")
        self.orders_tree.heading('model', text="Model")
        self.orders_tree.heading('price', text="Total Price")
        self.orders_tree.heading('location', text="Address")
        
        self.showOrder()
        
        self.delete_btn=Button(self.orders_tab, text="Delete", font=('Calibri', 11,"bold"), fg="white",background='#C31616',width=15, bd=1,command=self.del_order)
        self.delete_btn.place(x=10,y=390)

        self.wn.mainloop()

    #=============================Button functions for add cars tab===============================#

    def addCar(self):
        brnd=self.ent_cbrand.get()
        mdl=self.ent_cmodel.get()
        prc=self.ent_cprice.get()
        add=self.combo_address.get()

        if self.admin.addCars(brnd,mdl,prc,add):
            messagebox.showinfo("Item", "Item Added")
            self.show_cars_tree()
            
        else:
            messagebox.showerror("Error", "Item cannot be added")

    def update_cars(self):
        brand = self.ent_cbrand.get()
        model = self.ent_cmodel.get()
        price = self.ent_cprice.get()
        add=self.combo_address.get()

        if self.item_index=="":
             messagebox.showerror("Error", "Select a row first")

        elif self.validate():
            if self.admin.update_item(self.item_index, brand, model, add,price):
                messagebox.showinfo("Cars", "Car detail Updated")
                self.show_cars_tree()
            else:
                messagebox.showerror("Error", "Item cannot be updated")

    def reset(self):
        self.ent_cbrand.delete(0, END)
        self.ent_cmodel.delete(0, END)
        self.ent_cprice.delete(0, END)
        self.combo_address.delete(0, END)

    def del_cars(self):
        index=self.item_index
        ans=messagebox.askquestion("Delete","Are you sure?")
        if ans=="yes":
            if self.admin.delete_item(index):
                messagebox.showinfo("Sucess", "Item deleted")
                self.show_cars_tree()
            else:
                messagebox.showerror("Error", "Item cannot be deleted")
                self.show_cars_tree()                
        else:
            messagebox.showerror("Error", "Item not deleted")

    def show_cars_tree(self):
        self.cars_tree.delete(*self.cars_tree.get_children())
        data = self.admin.show_cars()
        for i in data:
            self.cars_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3],i[4]))
        self.cars_tree.bind("<Double-1>", self.select_item)

    def select_item(self, event):
        selected_item = self.cars_tree.selection()[0]
        self.item_index = self.cars_tree.item(selected_item, 'text')
        item_data = self.cars_tree.item(selected_item, 'values')
        self.ent_cbrand.delete(0, END)
        self.ent_cbrand.insert(0, item_data[0])
        self.ent_cmodel.delete(0, END)
        self.ent_cmodel.insert(0, item_data[1])
        self.ent_cprice.delete(0, END)
        self.ent_cprice.insert(0, item_data[2])
        self.combo_address.delete(0, END)
        self.combo_address.insert(0, item_data[3])

    def validate(self):
        brand = self.ent_cbrand.get()
        model = self.ent_cmodel.get()
        price = self.ent_cprice.get()
        add= self.combo_address.get()

        if brand=='' or model=='' or price=='' or add=='':
            messagebox.showerror("Error", "Dont leave Entry field Empty")
            return False

        elif not price.isdigit():
            messagebox.showerror("Error", "Add valid rate")
            return False
        else:
            return True
    
    def exitWn(self):
        self.wn.destroy()
        
    #================================Button function for User register Tab=============================#
    def reset_val(self):
        self.combo_type.set('')
        self.ent_username.delete(0, END)
        self.ent_pass.delete(0, END)
        self.ent_name.delete(0, END)
        self.ent_add.delete(0, END)
        self.ent_phone.delete(0, END)
        self.ent_email.delete(0, END)

    def rgstr_btn(self):
        un = self.ent_username.get()
        pw= self.ent_pass.get()
        n = self.ent_name.get()
        a = self.ent_add.get()
        p = self.ent_phone.get()
        e =self.ent_email.get()
        t = self.combo_type.get()
        
        if self.validateUser():
            ans=messagebox.askquestion("Confirm Registration","Are you sure?")
            if ans=="yes":
                if self.user.register(un,pw,n,a,p,e,t):
                    messagebox.showinfo("Sucess", "User registered")
                else:
                    messagebox.showerror("Error", "Can't register")


    def validateUser(self):
        un = self.ent_username.get()
        pw= self.ent_pass.get()
        n = self.ent_name.get()
        a = self.ent_add.get()
        p = self.ent_phone.get()
        e =self.ent_email.get()
        t = self.combo_type.get()

        if un=='' or pw=='' or n=='' or a=='' or p=='' or e=='' or t=='':
            messagebox.showerror("Error", "Please enter all the data")
            return False

        elif self.user.checkUser(un):
            messagebox.showerror("Error", "Username already taken")
            return False

        else:
            return True

    #================================Functions for show orders tab==========================================#
    
    def del_order(self):
        oid=self.orders_tree.item(self.orders_tree.selection()[0], 'text')
        if self.admin.delete_order(oid):
            messagebox.showinfo("Deleted","Order Removed")
            self.showOrder()
        else:
            messagebox.showerror("Error","Couldn't Delete")
            self.showOrder()

    def showOrder(self):
        self.orders_tree.delete(*self.orders_tree.get_children())
        data=self.admin.show_orders()
        for i in data:
            total=i[6]*i[7]
            self.orders_tree.insert("", "end",text=i[0] , value=(i[1], i[2], i[3],i[4],i[5],i[6],total))


    #============================Functions for User Details Tab========================================#
    def show_menu(self):
        my_menu = Menu(self.wn)
        self.wn.config(menu=my_menu)
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_cascade(label="View Parking details",command=self.openParking)
        file_menu.add_cascade(label="Exit",command=self.wn.destroy)

    def searchDetails(self):
        name=self.ent_user.get()
        print(name)
        data=self.user.showDetails(name)

    def openParking(self):
        iv=adminParking.parkDetails()


  
        




# iv=addCars()