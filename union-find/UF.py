class UF(object):
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0

    def count(self):
        return self.count

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)
