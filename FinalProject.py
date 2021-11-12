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

def userPicks():
    user = input("Do you want to see the list of items or prices of the items?")
    if user == 'P':
        print(UserItems())
    elif user =='F':
        print("Hello")

if __name__ == "__main__":
    print(userPicks())