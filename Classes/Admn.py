import connection


class Admin:
    """This class contains the methods that is used by the admin of the system"""
    def __init__(self):
        self.db = connection.MyDb()

    def addCars(self,brnd,mdl,prc,add):
        self.__brand=brnd
        self.__model=mdl
        self.__price=prc
        self.__caddress=add
    
        try:
            qry = "INSERT INTO cars (cbrand,cmodel,cprice,caddress) VALUES (%s,%s,%s,%s)"
            values = (self.__brand,self.__model,self.__price,self.__caddress)
            self.db.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def show_cars(self):
        cars=[]
        try:
            qry = "SELECT * FROM cars"
            cars = self.db.show_data(qry)
            # print(cars)
            return cars
            # if len(cars) > 0:
            #     return True
            # else:
            #     return False
        except Exception as e:
            print(e)
            return cars
            # return False

    def update_item(self, index, brnd,mdl,add,prc):
        self.__brand=brnd
        self.__model=mdl
        self.__caddress=add
        self.__price=prc
        
        try:
            qry = "UPDATE cars SET cbrand = %s, cmodel = %s, cprice = %s , caddress=%s WHERE cid=%s"
            values = (self.__brand,self.__model,self.__price,self.__caddress, index)
            self.db.iud(qry, values)
            return True
        except Exception as e:
            print(e)
            return False

        

    def delete_item(self, index):

        try:
            qry = "DELETE FROM cars WHERE cid=%s"
            values = index
            self.db.iud(qry, (values,))
            return True
        except Exception as e:
            print(e)
            return False


    def search_items(self,key):
        items=[]
        try:
            qry= "select * from cars where cbrand LIKE  '%"+ key + "%'"
            items=self.db.show_data(qry)
            return items
            # if len(items) > 0:
            #     return True
            # else:
            #     return False
            
        except Exception as e:
            print(e)
            return items
            # return False


    def show_orders(self):
        data=[]
        try:
            qry = "select orders.orderId,orders.username, cars.cbrand,cars.cmodel, orders.pickUpDate,cars.caddress, orders.days,  cars.cprice from orders join cars on orders.cid = cars.cid;"
            data = self.db.show_data(qry)
            # print(cars)
            return data
            # if len(items) > 0:
            #     return True
            # else:
            #     return False
        except Exception as e:
            print(e)
            return data
            # return False
    def delete_order(self,oid):
        try:
            qry="delete from orders where orderId=%s"
            values=oid
            self.db.iud(qry, (values,))
            return True
        except Exception as e:
            print(e)
            return False

