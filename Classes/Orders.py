import connection

class Order:
    def __init__(self):
        self.db=connection.MyDb()


    def add_order(self,cid,pdate,days,user):
        self.__cid=cid
        self.__pdate=pdate
        self.__days=days
        self.__user=user
        # self.__caddress=add
        try:
            qry = "INSERT INTO orders (username,cid, PickupDate, days) VALUES (%s,%s, %s, %s)"
            values = (self.__user,self.__cid,self.__pdate,self.__days)
            self.db.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    # def delete_order(self):
    #     pass

    def all_address(self):
        qry="select distinct caddress from cars"
        result=self.db.show_data(qry)
        return result

    def searchBy_Add(self,key):
        qry= "select * from cars where caddress LIKE  '%"+ key + "%'"
        items=self.db.show_data(qry)
        return items
        

    def showOrder(self, uname):
        self.__user= uname
        qry= "select orders.orderId,orders.username, cars.cbrand,cars.cmodel, orders.pickUpDate,cars.caddress, orders.days,  cars.cprice from orders join cars on orders.cid = cars.cid where orders.username=%s"
        values= self.__user
        result=self.db.show_data1(qry, (values,))
        return result