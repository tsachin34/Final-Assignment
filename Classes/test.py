import sys

import unittest

sys.path.append("D:/Second Semester/Algorithm/python/Online/finalAssignment/Classes")

import Admn
import Orders
import parking
import userData

class test(unittest.TestCase):



    def testAddcars(self):
        
        actual_result= self.admin.addCars("test","test","1","test")
        self.assertTrue(actual_result)
        

    def testDeleteOrder(self):
        actual_result= self.admin.delete_order(1)
        self.assertTrue(actual_result)

    def testShowCars(self):
        self.admin = Admn.Admin()
        actual_result= self.admin.show_cars()
        self.assertTrue(actual_result)


    def testupdateItem(self):
        self.admin = Admn.Admin()
        actual_result= self.admin.update_item(1,"test","test","1","test")
        self.assertTrue(actual_result)

    def testdeleteItem(self):
        self.admin = Admn.Admin()
        actual_result= self.admin.delete_item(1)
        self.assertTrue(actual_result)





        






# iv=test()
# iv.testShowCars()