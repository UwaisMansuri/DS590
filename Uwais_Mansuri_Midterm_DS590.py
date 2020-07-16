#  4 .  Create two singly linked lists and write a Python program to
#  find the intersection node between the two linked lists.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.ll = list()

    def insert(self, data):
        newnode = Node(data)
        currentnode = self.head
        if currentnode.data == None:
            self.head = newnode
            self.ll.append(self.head)
        else:
            while currentnode.next != None:
                self.ll.append(currentnode)
                currentnode = currentnode.next
            currentnode.next = newnode
            self.ll.append(newnode)

    def printlist(self):
        for i in self.ll:
            print(i.data)

def intersection_node(ll1,ll2):
    for i in ll1:
        for j in ll2:
            if i.data == j.data:
                print("The intersecting node: " + str(i.data))

ll1 = LinkedList()
ll2 = LinkedList()
ll1.insert(1)
ll1.insert(4)
ll1.insert(7)
ll1.insert(9)
ll2.insert(2)
ll2.insert(3)
ll2.insert(7)
ll2.insert(8)
intersection_node(ll1.ll, ll2.ll)

#  5. Write a Python program to find the second largest element in an array.
import numpy as np
x=np.array([1,5,6,4,3,2])
x.sort()
print('The sorted array is: ' +str(x))
n = len(x)
print('The second largest no is ' + str((x[n-2])))

#  6. Write a Python program to find out whether a given string of parenthesis and brackets is balanced.

def check(input):
    brackets = [0, 0, 0, 0, 0, 0] #  Format ['(', '[', '{', ')', ']', '}']
    for i in input:
        if i == '(':
            brackets[0] += 1
        elif i == '[':
            brackets[1] += 1
        elif i == '{':
            brackets[2] += 1
        elif i == ')':
            brackets[3] += 1
        elif i == ']':
            brackets[4] += 1
        elif i == '}':
            brackets[5] += 1
    if brackets[0] != brackets[3] or brackets[1] != brackets[4] or brackets[2] != brackets[5]:
        print("Unbalanced string")
    else:
        print("Balanced string")

input = "{[()]}"
check(input)

#  7.  Write a Python program to detect a loop in a linked list. Returns True/False.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.ll = list()

    def insert(self, data):
        newnode = Node(data)
        currentnode = self.head
        if currentnode.data == None:
            self.head = newnode
            self.ll.append(self.head)
        else:
            while currentnode.next != None:
                self.ll.append(currentnode)
                currentnode = currentnode.next
            currentnode.next = newnode
            self.ll.append(newnode)

    def printlist(self):
        for i in self.ll:
            print(i.data)

def check_loop(ll):
    currentnode = ll.head
    count = 0
    while currentnode.next != None:
        count += 1
        currentnode = currentnode.next
        if count >= len(ll.ll):
            return True
    return False

ll = LinkedList()
ll.insert(2)
ll.insert(3)
ll.insert(5)
print(check_loop(ll))

#  8.  Write a Python program to reverse a singly linked list both recursively and iteratively.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self): #  By iteration
        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def reverse_rec(self): #  By recursion
        prev = None
        current = self.head
        self.rec_helper(prev, current)

    def rec_helper(self, prev, current):
        if current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            self.rec_helper(prev, current)
        else:
            self.head = prev

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        self.reverse()
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


ll = LinkedList()
ll.insert(1)
ll.insert(3)
ll.insert(6)
ll.insert(8)
ll.print_list()
print()
ll.reverse_rec()
ll.print_list()
