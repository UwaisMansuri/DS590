import sys

class MaxHeap:

    def __init__(self, max):
        self.max = max
        self.size = 0
        self.BHM = [0] * (self.max + 1)
        self.BHM[0] = sys.maxsize #  For restricting the size of the list

    def parent_node(self, i):
        return i // 2

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return (2 * i) + 1

    def insert(self, i):
        if self.size >= self.max:
            return
        self.size += 1
        self.BHM[self.size] = i

        self.sift_up(self.size)

    def sift_up(self, current_node):
        while self.BHM[current_node] > self.BHM[self.parent_node(current_node)]:
            self.BHM[current_node], self.BHM[self.parent_node(current_node)] = \
                self.BHM[self.parent_node(current_node)], self.BHM[current_node] #  Swapping current node woth its
                                                                                # parent node
            current_node = self.parent_node(current_node)

    def print_heap(self):
        for i in range(1, (self.parent_node(self.size)) + 1):
            print(" P: " + str(self.BHM[i]) + " L: " +
                  str(self.BHM[self.left_child((i))]) + " R: " +
                  str(self.BHM[self.right_child(i)]))


BHMAX = MaxHeap(15)
BHMAX.insert(42)
BHMAX.insert(29)
BHMAX.insert(18)
BHMAX.insert(14)
BHMAX.insert(7)
BHMAX.insert(18)
BHMAX.insert(12)
BHMAX.insert(11)
BHMAX.insert(5)
BHMAX.print_heap()