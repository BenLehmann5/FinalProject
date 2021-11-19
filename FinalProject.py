'''
Author: Ben Lehmann
Date: 11/1 - Not Done


'''

from tkinter import *

class GroceryList:
    def __init__(self):
        self.items = []

    def checkEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.insert(0,item)

    def adding(self,item):
        self.items.append(item)

    def remove(self):
        self.items.pop()

    def length(self):
        return len(self.items)

class Prices:
    def __init__(self):
        self.queue = []
    def enqueue(self,cost):
        self.queue.append(cost)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def CostSize(self):
        return len(self.queue)

    def cost(self,user_prices):
        total = 0
        for value in user_prices:
            total = total + value
        return total

def UserItems():
    grocery = GroceryList()
    i = 0
    while 1:
        i += 1
        items = input('Enter item %d: ' % i)
        if items == '':
            break
        grocery.adding(items)
    print(grocery.items)
    addOr = input("Do you want to add another or delete? Enter 'Add' or 'Delete: ")
    if(addOr == 'Add'):
        added = input('Enter the item')
        grocery.adding(added)
        print(grocery.items)
    elif(addOr == 'Delete'):
        grocery.remove()
        print(grocery.items)
    return

def UserCost():
    cost = Prices()
    i = 0
    while 1:
        i += 1
        items = float(input('Enter Price %d: ' % i))
        if items == 0:
            break
        cost.enqueue(items)
    print(cost.queue)

class UserAndCost:
    def __init__(self):
        self.dic = {}

    def add(self,key,value):
        self[key] = float(value)

    def print_value(self):
        for k,v in self.dic.items():
            print(k + " : " + v)


def combine():
    cost_item = UserAndCost()
    user_x = int(input("Enter the Number of items"))
    for x in range(user_x):
        item = input('Enter your item')
        cost = input('Enter your price')
        cost_item.add(item,cost)
    cost_item.print_value()

def InsertionSort(userList):
    for i in range(1, len(userList)):
        currentVal = userList[i]
        pos = i
        while pos>0 and userList[pos-1]>currentVal:
            userList[pos]=userList[pos-1]
            pos=pos-1
        userList[pos] = currentVal


if __name__ == "__main__":
    print(combine())