'''
Author: Ben Lehmann
Date: 11/1 - Not Done
Function: Ask the user to either add item names, or prices or even both

Data Structures: Queues, Map, Stack
Algorithm: Insertion Sort

10/28 - Standup #1
11/04 - Standup #2
11/10 - Standup #3
11/17 - Standup #4



'''


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

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue)

    def enqueue(self,cost):
        self.queue.append(cost)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

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
        return grocery.items
    elif(addOr == 'Delete'):
        grocery.remove()
        return grocery.items
    return "Your List: " + str(grocery.items)

def UserCost():
    cost = Prices()
    print("Enter your prices and then type '0.0' to finish")
    i = 0
    while 1:
        i += 1
        items = float(input('Enter Price %d: ' % i))
        if items == 0.00:
            break
        cost.enqueue(items)
    return(cost.queue)

def userTotal():
    cost = Prices()
    print("Enter your prices and then type '0.0' to finish")
    i = 0
    while 1:
        i += 1
        items = float(input('Enter Price %d: ' % i))
        if items == 0.00:
            break
        cost.enqueue(items)
    return(cost.queue)

class UserAndCost:
    def __init__(self):
        self.dic = {}

    def add(self,key,value):
        self[key] = value

    def print_value(self):
        print("Items------------")
        for k,v in self.dic.items():
             print(k + " : " + v)
        return

    def total(self):
        totals = self.dic.values()
        print(str(sum(totals)))

def combine():
    cost_item = UserAndCost()
    user_x = int(input("Enter the Number of items:  "))
    for x in range(user_x):
        item = input('Enter your item: ')
        cost = input('Enter your price: ')
        cost_item.dic[item] = cost
    cost_item.print_value()


def InsertionSort(userList):    #I was between Selection Sort or Insertion sort, tried both, tested them and Insertion was better
    for i in range(1, len(userList)):
        currentVal = userList[i]
        pos = i
        while pos>0 and userList[pos-1]>currentVal:
            userList[pos]=userList[pos-1]
            pos=pos-1
        userList[pos] = currentVal


def UserSelection():
    user = input("Do You Want to Enter Prices or Enter Items, Press P for Prices or I for Item or B for Both:  ")
    if user == 'i':
        items = UserItems()
        return items
    elif user == 'p':
        cost = UserCost()
        print(cost)
        InsertionSort(cost)
        print(cost)
        return "Cost $" + str(sum(cost))
    elif user == 'b':
        user_items = combine()
        print(user_items)
    else:
        return None

if __name__ == "__main__":
    print(UserSelection())