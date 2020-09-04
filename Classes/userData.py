import connection
class User:
    """The methods of this class performs the function of User Registration"""

    def __init__(self):
        self.db=connection.MyDb()
        
        
    def register(self,un,pw,n,a,p,e,t):
        self.__username=un
        self.__password=pw
        self.__name=n
        self.__address=a
        self.__phone=p
        self.__email=e
        self.__type=t
        qry="Insert into users(username,password,name,address,phone,email,type) values(%s,%s,%s,%s,%s,%s,%s)"
        values=(self.__username,self.__password,self.__name, self.__address,
         self.__phone, self.__email, self.__type )
        self.db.iud(qry,values)
        return True


    def login(self,un,pw):
        qry="Select * from users where username=%s AND password=%s"
        values=(un,pw)
        user=self.db.show_data1(qry,values)
        # print(type(user))
        return user


    def checkUser(self,key):
        """This method checks if the entered username is already registered or not
        inorder to prevent duplicate usernames"""
        qry="select username from users order by username "
        data=self.db.show_data(qry)
        if self.iterativeSearch(data,key)>=0:
            return True
        else:
            return False

    def iterativeSearch(self,list,key):
        start=0
        end=len(list)-1
        while start<=end:
            mid=(start+end)//2
            if list[mid][0]==key:
                return mid
            
            elif list[mid][0]>key:
                end= mid - 1
            
            else:
                start=mid+1
        return -1
        

