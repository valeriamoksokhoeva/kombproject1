class UnionFind:
    def __init__(self, size):
        # инициализация массивов для хранения родителей и рангов
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        # поиск корня элемента с сжатием путей
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # сжимаем путь
        return self.parent[x]

    def union(self, x, y):
        # объединение двух множеств
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # объединение по рангу
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        # проверка, принадлежат ли два элемента одному множеству
        return self.find(x) == self.find(y)

# пример
uf = UnionFind(10) 
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)

# проверяем соединенность элементов
print(uf.connected(1, 3))  # True, так как 1 и 3 объединены через 2
print(uf.connected(1, 4))  # False, так как 1 и 4 находятся в разных множествах