import connection

class Park:
    """This class performs the function of parking system"""
    def __init__(self):
        self.db = connection.MyDb()

    def add_spot(self,spot):
        self.__spot=spot
        try:
            qry="insert into parking_detail(spot_no) values(%s)"
            values=(self.__spot)
            self.db.iud(qry, (values,))
            return True

        except Exception as e:
            print(e)
            return False

    def confirm_parking(self,usr,brnd,mdl,typ,spot,arvl):
        self.__user=usr
        self.__brand=brnd
        self.__model=mdl
        self.__type=typ
        self.__spot=spot
        self.__arrival=arvl
        
        try:
            qry="insert into parking(username,cbrand,cmodel,vechile_type,parking_spot,arrival) values(%s,%s,%s,%s,%s,%s)"
            values=(self.__user,self.__brand,self.__model, self.__type,self.__spot,self.__arrival)
            self.db.iud(qry, values)
            return True

        except Exception as e:
            print(e)
            return False

    def avilable_spots(self):
        qry= "select spot_no from parking_detail where spot_no NOT IN (select parking_detail.spot_no from parking_detail  join parking  on parking_detail.spot_no=parking.parking_spot)"
        result=self.db.show_data(qry)
        return result
    
    def spotUnavilable(self):
        qry= "select spot_no from parking_detail where spot_no NOT IN (select parking_detail.spot_no from parking_detail  join parking  on parking_detail.spot_no=parking.parking_spot)"
        result=self.db.show_data(qry)
        if len(result)==0:
            return True
        else:
            return False

    def showData(self):
        qry='select pid,username,cbrand,cmodel,vechile_type,parking_spot,arrival from parking_detail  join parking  on parking_detail.spot_no=parking.parking_spot'
        result=self.db.show_data(qry)
        return result

    def delete_booking(self,index):
        try:
            qry='delete from parking where pid=%s'
            values = index
            self.db.iud(qry, (values,))
            return True
        except Exception as e:
            print(e)
            return False




        

    