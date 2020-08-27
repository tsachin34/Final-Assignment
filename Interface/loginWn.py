import sys

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import userMenu


sys.path.append("D:/Second Semester/Algorithm/Assignment Draft/Classes")
# sys.path.append("D:/Second Semester/Algorithm/python/Online/finalAssignment/images")
from userData import *
import adminWn


class Log:
    """ This class is made to buid a proper Login System"""
    def __init__(self):
        """This is an intialization method to add attributes"""
        self.wn=Tk()
        self.wn.title("User login")
        self.wn.iconbitmap(r"D:\Second Semester\Algorithm\python\Online\finalAssignment\icons\carIcon.ico")
        self.wn.geometry("520x300+300+100")
        self.wn.configure(background="#041E77")
        

        
        self.user=User()
        # self.admin=adminWn.addCars()

        #============String Variable=========================#
        self.un = StringVar()
        self.pw = StringVar()
        #===========label====================================#

        
        # self.lb_head=Label(self.wn,text="Log In",fg="white",bg="#2C0B47",font=("Verdana",20,"bold"))
        # self.lb_head.place(x=0,y=0,relwidth=1)

        #===========Frame=========================================#
        self.frame1=Frame(self.wn)
        self.frame1.place(x=100,y=80)
        self.frame1.configure(background="#041E77")

        #==========All images=====================================#
        

        self.login_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/Assignment Draft/images/userICon.png").resize((60,65)))
        self.login_label=Label(self.wn,image=self.login_image,background="#041E77")
        self.login_label.place(x=230,y=10)
        
        self.user_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/Assignment Draft/images/manUser.png").resize((35,35)))
        self.user_label=Label(self.frame1,image=self.user_image,background='#041E77')
        self.user_label.grid(row=0,column=0)

        self.password_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/Assignment Draft/images/pass4.png").resize((35,35)))
        self.password_label=Label(self.frame1,image=self.password_image,background='#041E77')
        self.password_label.grid(row=1,column=0)

        self.eye_image=ImageTk.PhotoImage(Image.open("D:/Second Semester/Algorithm/Assignment Draft/images/eye1.png").resize((30,30)))


        #==================Entryyy=================================#
        self.ent_username=Entry(self.frame1,font=("Verdana",14),textvariable=self.un)
        self.ent_username.grid(row=0,column=2,padx=10,pady=10)
        self.ent_username.insert( 0,"Username")
        self.ent_username.bind("<1>", self.entry_user)

        self.ent_pass=Entry(self.frame1,font=("Verdana",14),textvariable=self.pw)
        self.ent_pass.grid(row=1,column=2,pady=10)
        self.ent_pass.insert( 0,"Password")
        self.ent_pass.bind("<1>", self.entry_pw)
        
       #=================buttons=====================================#
        self.btn = Button(self.frame1, text='Log in', font=('Calibri', 14,"bold"), fg="white",background='#041E77',width=20, bd=0.5, command=self.login_onclick)
        self.btn.grid(row=2,column=2,pady=10)

        self.btn4= Button(self.frame1,text="Exit",font=('Calibri', 14,"bold"), fg="white",background='red',width=20, bd=0.5, command=self.login_onclick)
        self.btn4.grid(row=3,column=2,pady=5)

        self.btn5= Button(self.frame1,image=self.eye_image,background='#041E77',activebackground='#041E77',borderwidth=0 )
        self.btn5.grid(row=1,column=3)

        self.wn.mainloop()
    
    def entry_user(self,event):
        """This method unbinds the username entry to make it writable"""
        self.un.set("")
       
        self.ent_username.unbind("<1>")
    

    def entry_pw(self,event):
        """This method unbinds the password entry to make it writable"""
        self.pw.set("")
        self.ent_pass.unbind("<1>")
        self.ent_pass=Entry(self.frame1,show='*',font=("Verdana",14),textvariable=self.pw)
        self.ent_pass.grid(row=1,column=2,padx=10,pady=10)
        self.btn5.bind("<Button-1>", self.show)

    def show(self,event):
        """This method shows the hidden password when the button is triggered"""
        self.ent_pass=Entry(self.frame1,show='',font=("Verdana",14),textvariable=self.pw)
        self.ent_pass.grid(row=1,column=2,padx=10,pady=10)
        self.btn5.bind("<1>", self.hide)

    def hide(self,event):
        """This method hides the password when button is triggered"""
        self.ent_pass=Entry(self.frame1,show='*',font=("Verdana",14),textvariable=self.pw)
        self.ent_pass.grid(row=1,column=2,padx=10,pady=10)
        self.btn5.bind("<1>", self.show)


    def login_onclick(self):
        """This method is created to verify the username and password to open the next window"""
        un=self.un.get()
        pw=self.pw.get()
        user=self.user.login(un,pw)
        # print(user)
        if len(user)>0:
            messagebox.showinfo("ok","logged in")
            self.wn.destroy()
            if user[0][7] == 'Admin':
                self.admin=adminWn.Cars()
            else:
                userMenu.userInterface(user[0])
        else:
            messagebox.showerror("Sorry","Wrong Username or Password")

iv=Log()
