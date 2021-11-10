'''
Author: Ben Lehmann
Date: 11/1 - Not Done


'''


from tkinter import *

class GroceryList:
    grocery = []

    def create(self,shopping,item):
        for i in shopping:
            grocery.insert(END,i[0] + " - " + str(i[1]))

    def Index(self,shopping,item):
        ind = -1
        for i in range(len(shopping)):
            if shopping[i][0] == item:
                ind = i
        return ind

    def removeLst(self,shopping,index):
        del(shopping[index])




