#  1. Operations for the Doubly Linked List in Python.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def insertEnd(self,newNode):
        if self.head is None:
            self.head=newNode
            return
        currentNode=self.head
        while True:
            if currentNode.next is None:
                break
            currentNode=currentNode.next
        currentNode.next=newNode
        newNode.previous=currentNode

    def insertAt(self,newNode,position):
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition==position:
                currentNode.previous.next= newNode
                newNode.previous=currentNode.previous
                newNode.next=currentNode
                currentNode.previous=newNode
                break
            currentNode=currentNode.next
            currentPosition += 1

    def insertHead(self,newNode):
        previousHead=self.head
        self.head=newNode
        self.head.next=previousHead
        previousHead.previous=self.head

    def deleteHead(self):
        self.head=self.head.next
        self.head.previous.next=None
        self.head.previous=None

    def deleteEnd(self):
        currentNode=self.head
        while True:
            if currentNode.next.next is None:
                currentNode.next.previous=None
                currentNode.next.next=None
                currentNode.next=None
                break
            currentNode=currentNode.next

    def printlist(self):
        if self.head is None:
            print('List is empty')
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

print('insertEnd/pushBack:')
nodeOne=Node('Uwais')
nodeTwo=Node('Jeet')
nodeThree=Node('Raj')
linkedList=Linkedlist()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.printlist()
print()

print('InsertHead/pushFront:')
nodeOne=Node('Uwais')
nodeTwo=Node('Jeet')
nodeThree=Node('Raj')
linkedList=Linkedlist()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertHead(nodeThree)
linkedList.printlist()
print()

print('deleteEnd/popBack:')
nodeOne=Node('Uwais')
nodeTwo=Node('Jeet')
nodeThree=Node('Raj')
linkedList=Linkedlist()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.deleteEnd()
linkedList.printlist()
print()

print('deleteHead/popFront:')
nodeOne=Node('Uwais')
nodeTwo=Node('Jeet')
nodeThree=Node('Raj')
linkedList=Linkedlist()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.deleteHead()
linkedList.printlist()
print()

print('insertAt (Add Before/after):')
nodeOne=Node('Uwais')
nodeTwo=Node('Jeet')
nodeThree=Node('Raj')
nodeFour=Node('Kusum')
linkedList=Linkedlist()
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertAt(nodeFour,2)
linkedList.printlist()
print()

#  2. Implement Push/Top/Pop/Empty operations for Stack in Python.
class Stack:
    def __init__(self):
        self.stack_list = list()

    def push(self, data):
        self.stack_list.append(data)
        print("Pushed " +  data + " into the stack!")

    def pop(self):
        print("Popped " + self.stack_list.pop() + " from the stack!")

    def top(self):
        print(self.stack_list[-1] + " is at the top of the stack!")

    def empty(self):
        while self.stack_list:
            self.pop()

    def print_stack(self):
        if not self.stack_list:
            print("The stack is empty!")
        else:
            print("The stack is: ")
            print("--------------")
            for i in self.stack_list:
                print(i)
                print("--------------")

print('Push/Top/Empty operations for Stack:')
stack_obj = Stack()
stack_obj.push("Uwais")
stack_obj.push("Jeet")
stack_obj.push("Raj")
stack_obj.push("Name")
stack_obj.print_stack()
stack_obj.top()
stack_obj.empty()
stack_obj.print_stack()
print()

print('Pop operations for Stack:')
stack_obj = Stack()
stack_obj.push("Uwais")
stack_obj.push("Jeet")
stack_obj.push("Raj")
stack_obj.push("Name")
stack_obj.print_stack()
stack_obj.pop()
stack_obj.pop()
stack_obj.pop()
stack_obj.print_stack()
print()


#  3. Implement Enqueue/Dequeue/Empty operations for Queue in Python.
class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        print(self.queue.pop(0) + " has been dequeued!")

    def print_queue(self):
        if not self.queue:
            print("The queue is empty!")
        else:
            self.queue = [i for i in reversed(self.queue)] #Reversing as queue follows the LIFO(Last In First Out) approach.
            print("The queue is:")
            print("-------------")
            for i in self.queue:
                print(i)
                print("-------------")
            self.queue = [i for i in reversed(self.queue)]

    def empty(self):
        while self.queue:
            self.dequeue()

print('Enqeue/Deqeue:')
queue_obj = Queue()
queue_obj.enqueue("Uwais")
queue_obj.enqueue("Jeet")
queue_obj.enqueue("Raj")
queue_obj.enqueue("Name")
queue_obj.print_queue()
queue_obj.dequeue()
queue_obj.dequeue()
queue_obj.dequeue()
queue_obj.dequeue()
print()

print('Empty operation: ')
queue_obj = Queue()
queue_obj.enqueue("Uwais")
queue_obj.enqueue("Jeet")
queue_obj.enqueue("Raj")
queue_obj.enqueue("Name")
queue_obj.print_queue()
queue_obj.empty()
queue_obj.print_queue()
