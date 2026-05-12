class Ubion_by_rank:
    def __init__(self):
        self.pred = {}
        self.rank = {}

    def make_set(self, x):
        self.pred[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if self.pred[x] != x:
            self.pred[x] = self.find_set(self.pred[x])
        return self.pred[x]

    def link(self, x, y):
        if self.rank[y] < self.rank[x]:
            self.pred[y] = x
        else:
            self.pred[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] = self.rank[y] + 1
