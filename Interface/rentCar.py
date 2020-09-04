import sys

from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import messagebox 
from tkcalendar import DateEntry

sys.path.append("D:/Second Semester/Algorithm/Assignment Draft/Classes")
import Admn
import Orders
import userMenu
import userParking

class placeOrder:
    """This class contains method and attributes of the system that allows user to rent a car"""
    def __init__(self,user):
        self.wn=tk.ThemedTk()
        self.wn.configure(bg="#6262ED")
        self.wn.title("Rent a car")
        self.wn.geometry("650x450+200+50")

        self.item_index = ""
        self.my_index = 1

        self.user=user

        self.wn.get_themes()
        self.wn.set_theme('plastik')

        self.item=Admn.Admin()
        self.order=Orders.Order()

    #==========================Frame1==============================#
        self.frame1=Frame(self.wn)
        self.frame1.place(x=10,y=10)
        self.frame1.configure(bg="#6262ED")


        self.lbl_add=Label(self.frame1,font=("Calibri",14,"bold"),text="Address:",bg="#6262ED")
        self.lbl_add.grid(row=0,column=0)

        self.combo_tbl1 = ttk.Combobox(self.frame1, state='readonly',width=20)
        self.combo_tbl1.grid(row=0, column=1,padx=5)
        self.combo_tbl1['values'] = self.order.all_address()

        self.btn1 = Button(self.frame1, text='Search', font=('Calibri', 11,"bold"), fg="white",background='#6262ED',width=12, bd=1,command=self.search)
        self.btn1.grid(row=0,column=2,padx=10)

    #==========================Frame2==============================#
        self.frame2=Frame(self.wn,bg="#6262ED")
        self.frame2.place(x=10,y=50)

        self.cars_tree = ttk.Treeview(self.frame2, columns=('Brand', 'Model', 'Price','Address'))
        self.cars_tree.grid(row=0,column=0)
        self.cars_tree['show'] = 'headings'
        self.cars_tree.column('Brand', width=150, anchor='center')
        self.cars_tree.column('Model', width=150, anchor='center')
        self.cars_tree.column('Price', width=150, anchor='center')        
        self.cars_tree.column('Address', width=155, anchor='center')
        self.cars_tree.heading('Brand', text="Brand")
        self.cars_tree.heading('Model', text="Model")
        self.cars_tree.heading('Price', text="Price")
        self.cars_tree.heading('Address', text="Address")
        self.cars_tree.bind("<Double-1>", self.select_item)

        self.vsb = ttk.Scrollbar(self.frame2, orient="vertical", command=self.cars_tree.yview)
        self.vsb.place(x=591, y=2, height=225)

        self.cars_tree.configure(yscrollcommand=self.vsb.set)

      #==========================Frame3==============================#
        self.frame3=Frame(self.wn,bg="#6262ED")
        self.frame3.place(x=10,y=300)

        self.lbl_brand=Label(self.frame3,font=("Calibri",14,"bold"),text="Brand:",bg="#6262ED")
        self.lbl_brand.grid(row=0,column=0)

        self.lbl_model=Label(self.frame3,font=("Calibri",14,"bold"),text="Model:",bg="#6262ED")
        self.lbl_model.grid(row=1,column=0)

        self.ent_cbrand=ttk.Entry(self.frame3,font=("Verdana",12),state="readonly")
        self.ent_cbrand.grid(row=0,column=1,padx=10)

        self.ent_cmodel=ttk.Entry(self.frame3,font=("Verdana",12),state="readonly")
        self.ent_cmodel.grid(row=1,column=1,padx=10)

        self.lbl_price=Label(self.frame3,font=("Calibri",14,"bold"),text="Price:",bg="#6262ED")
        self.lbl_price.grid(row=2,column=0)

        self.ent_cprice=ttk.Entry(self.frame3,font=("Verdana",12),state="readonly")
        self.ent_cprice.grid(row=2,column=1,padx=10)

        self.lbl_date=Label(self.frame3,font=("Calibri",14,"bold"),text="Pick up Date:",bg="#6262ED")
        self.lbl_date.grid(row=0,column=3)

        self.cal = DateEntry(self.frame3, width=12, background='darkblue',
                    foreground='white', borderwidth=2, state="readonly")
        self.cal.grid(row=0,column=4)

        self.lbl_days=Label(self.frame3,font=("Calibri",14,"bold"),text="Days:",bg="#6262ED")
        self.lbl_days.grid(row=1,column=3)

    
        self.combo_tbl2 = ttk.Combobox(self.frame3, state='readonly',width=11)
        self.combo_tbl2.grid(row=1, column=4,padx=5)
        self.combo_tbl2['values'] =['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

        self.btn1= Button(self.wn,text="Order",font=('Calibri', 11,"bold"), fg="white",background='#6262ED',borderwidth=0.5,width=15,command=self.submitOrder )
        self.btn1.place(x=260,y=400)

        self.show_menu()
                
        self.wn.mainloop()

    def search(self):
        key = self.combo_tbl1.get()
        items=self.order.searchBy_Add(key)
        self.cars_tree.delete(*self.cars_tree.get_children())
        for i in items:
            self.cars_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3],i[4]+', Nepal'))


    def select_item(self, event):
        self.ent_cbrand.configure(state="normal")
        self.ent_cmodel.configure(state="normal")
        self.ent_cprice.configure(state="normal")
        
        selected_item = self.cars_tree.selection()[0]
        self.item_index = self.cars_tree.item(selected_item, 'text')
        item_data = self.cars_tree.item(selected_item, 'values')
        self.ent_cbrand.delete(0, END)
        self.ent_cbrand.insert(0, item_data[0])
        self.ent_cmodel.delete(0, END)
        self.ent_cmodel.insert(0, item_data[1])
        self.ent_cprice.delete(0, END)
        self.ent_cprice.insert(0, item_data[2])
        self.ent_cbrand.bind("<1>", self.entry_bind)
        self.ent_cmodel.bind("<1>", self.entry_bind)
        self.ent_cprice.bind("<1>", self.entry_bind)

    def entry_bind(self,event):
        self.ent_cbrand.configure(state="readonly")
        self.ent_cmodel.configure(state="readonly")
        self.ent_cprice.configure(state="readonly")

    def show_menu(self):
        my_menu = Menu(self.wn, bg="#6262ED")
        self.wn.config(menu=my_menu)
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label="Menu", menu=file_menu)
        file_menu.add_cascade(label="Parking",command=self.openParking)
        file_menu.add_cascade(label="History",command=self.openHistory)
        file_menu.add_cascade(label="Log Out",command=self.logOut)

    def submitOrder(self):
        cid=self.cars_tree.item(self.cars_tree.selection()[0], 'text')
        date=self.cal.get_date()
        days= self.combo_tbl2.get()
        user=self.user[1]

        if self.order.add_order(cid,date,days,user):
            messagebox.showinfo("Ordered", "Order Placed")
        else:
            messagebox.showerror("Error", "Something went wrong")
    
    def openHistory(self):
        user= self.user
        self.wn.destroy()
        iv=userMenu.Transaction(user)

    def openParking(self):
        self.wn.destroy()
        iv=userParking.Parking(self.user)

    def logOut(self):
        ans=messagebox.askquestion("Log Out","Are you sure you want to log out?")
        if ans=="yes":
                self.wn.destroy()
                import loginWn
           

# iv=placeOrder()


