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


class GroceryList:   #We create a Stack for the Grocery List, easy to add and remove
    def __init__(self):
        self.items = []

    def checkEmpty(self):  #Check if the item is empty
        return self.items == []

    def push(self,item):  #We insert the user's item
        self.items.insert(0,item)

    def adding(self,item):
        self.items.append(item)

    def remove(self):  #We remove the user's item
        self.items.pop()

    def length(self):  #I did not need this, this we to check if the stack is empty
        return len(self.items)

class Prices:  #We create a Queue for Prices
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.size() == 0  #Check is queue is empty

    def size(self):  #Check the size to see if anything is in there
        return len(self.queue)

    def enqueue(self,cost):  #With Queues, we enqueue and dequeue, so we user append and pop
        self.queue.append(cost)
    def dequeue(self):
        if len(self.queue) < 1:  #If the queue is empty, we can't do anything, but if there is, we remove the front
            return None
        return self.queue.pop(0)

def UserItems():  #This method calls back the Stack Class
    grocery = GroceryList()
    i = 0
    while 1:  #We are going to iterate through until the user is done inputing items
        i += 1
        items = input('Enter item %d: ' % i)
        if items == '':
            break
        grocery.adding(items)  #We will use the adding() function from the GroceryList class
    print(grocery.items)
    addOr = input("Do you want to add another or delete? Enter 'Add' or 'Delete: ")  #We will give the chance of adding or removing from the stack
    if(addOr == 'Add'):
        added = input('Enter the item')
        grocery.adding(added)
        return grocery.items
    elif(addOr == 'Delete'):
        grocery.remove()
        return grocery.items
    return "Your List: " + str(grocery.items)

def UserCost():  #We use the Queue list here
    cost = Prices()
    print("Enter your prices and then type '0.0' to finish")
    i = 0
    while 1:
        i += 1
        items = float(input('Enter Price %d: ' % i))  #Most Grocery prices are floats, so I decided to keep these floats
        if items == 0.00:  #If the user is done, they type in 0.00, which means I have nothing else
            break  #We break from the loop
        cost.enqueue(items)
    return(cost.queue)

def userTotal():   #Disregard this Method
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

class UserAndCost:   #I decided to create a map structure to keep user's items and prices
    def __init__(self):
        self.dic = {}

    def add(self,key,value):  #This is how we add items to the map
        self[key] = value

    def print_value(self):  #We are going to return the map results
        print("Items------------")
        for k,v in self.dic.items():
             print(k + " : " + v)
        return

    def total(self):  #This is totals, disregard
        totals = self.dic.values()
        print(str(sum(totals)))

def combine():
    cost_item = UserAndCost()   #This is where we add the user's prices and items to the map, using a for loop
    user_x = int(input("Enter the Number of items:  "))
    for x in range(user_x):
        item = input('Enter your item: ')
        cost = input('Enter your price: ')
        cost_item.dic[item] = cost
    cost_item.print_value()


def InsertionSort(userList):    #I was between Selection Sort or Insertion sort, tried both, tested them and Insertion was better
    for i in range(1, len(userList)):  #If i in range (1 and the number of items in our list), the current value will be the current index
        currentVal = userList[i]  #Current val is the current index of the list
        pos = i  #Position of the list is index i
        while pos>0 and userList[pos-1]>currentVal: #If our position is not negative and the previous position of the list is still bigger than current
            userList[pos]=userList[pos-1]  #We will set our current pos index of the list to the previous index
            pos=pos-1
        userList[pos] = currentVal


def UserSelection():  #This is the main control, this tells the user everything and what to type in
    user = input("Do You Want to Enter Prices or Enter Items, Press P for Prices or I for Item or B for Both:  ")
    if user == 'i':
        items = UserItems()
        return items
    elif user == 'p':
        cost = UserCost()
        print(cost)
        InsertionSort(cost)  #We will sort out price, numerically order
        print(cost)
        return "Cost $" + str(sum(cost))
    elif user == 'b':
        user_items = combine()
        print(user_items)
    else:
        return None

if __name__ == "__main__":
    print(UserSelection())