#  5. QuickFindUF
class QuickFind:
    def __init__(self, max):
        self.id = list(range(max))
        self.size = [1] * max

    def root(self, x):
        while x != self.id[x]:
            self.id[x] = self.id[self.id[x]]
            x = self.id[x]
        return x

    def union(self, p, q):
        x = self.root(p)
        y = self.root(q)
        self.id[x] = y

    def find(self, p, q):
        return self.root(p) == self.root(q)


#  6. QuickUnionUF

class QuickUnion:
    def __init__(self, max):
        self.id = list()
        self.max = max
        for i in range(0, self.max):
            self.id.append(i)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j


print("Q5. UnionFind:")
connectivity_q5 = QuickFind(8)
connectivity_q5.union(3, 5)
connectivity_q5.union(4, 6)
print(connectivity_q5.find(4, 6))

print("Q6. QuickUnion:")
connectivity_q6 = QuickUnion(9)
connectivity_q6.union(1, 2)
connectivity_q6.union(3, 4)
print(connectivity_q6.connected(1, 2))
