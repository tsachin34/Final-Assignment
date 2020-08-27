import mysql.connector


class MyDb:
    def __init__(self):
        self.my_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Sachin2002',
        auth_plugin='mysql_native_password',
                        database="db_PMS"
                        )
        self.my_cursor = self.my_connection.cursor()

    def iud(self, qry, values):
        try:
            self.my_cursor.execute(qry,values)
            self.my_connection.commit()

        except Exception as e :
            print(e)

    
    def test(self, qry, values):
        self.my_cursor.execute(qry,values)
        self.my_connection.commit()
        return self.my_cursor.lastrowid

    def insert_with_id_return(self,qry,values):
        self.my_cursor.execute(qry,values)
        self.my_connection.commit()
        return self.my_cursor.lastrowid

    def show_data1(self, qry,values):
        self.my_cursor.execute(qry,values)
        data = self.my_cursor.fetchall()
        return data


    def show_data(self, qry):
        self.my_cursor.execute(qry)
        data = self.my_cursor.fetchall()
        return data


iv=MyDb()



