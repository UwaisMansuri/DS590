class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newNode

    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newNode

    def deleteHead(self):
        self.head=self.head.next


    def deleteEnd(self):
        lastnode=self.head
        while lastnode.next is not None:
            previousNode=lastnode
            lastnode=lastnode.next
        previousNode.next=None

    def printlist(self):
        if self.head is None:
            print("It is empty")
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next

#PushFront
firstNode = Node('Uwais')
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node('Jeet')
linkedList.insert(secondNode)
thirdNode = Node('Raj')
linkedList.insertHead(thirdNode)
linkedList.printlist()
print('\n')

#PushBack
firstNode = Node('Uwais')
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node('Jeet')
linkedList.insert(secondNode)
thirdNode = Node('Raj')
linkedList.insert(thirdNode)
linkedList.printlist()
print('\n')

#PopBack
firstNode = Node('Uwais')
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node('Jeet')
linkedList.insert(secondNode)
thirdNode = Node('Raj')
linkedList.insert(thirdNode)
linkedList.deleteEnd()
linkedList.printlist()
print('\n')

#PopFront
firstNode = Node('Uwais')
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node('Jeet')
linkedList.insert(secondNode)
thirdNode = Node('Raj')
linkedList.insert(thirdNode)
linkedList.deleteHead()
linkedList.printlist()


