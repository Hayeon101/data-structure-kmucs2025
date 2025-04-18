class Set:
    def __init__(self):
        self.capacity = 30
        self.size = 0
        self.array = [None] * self.capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insertElement(self, e):
        if not self.isFull():
            for i in range(self.size):
                if self.array[i] == e:
                    return
            for i in range(self.size):
                if self.array[i] >= e:
                    for j in range(self.size, i, -1):
                        self.array[j] = self.array[j-1]
                    self.array[i] = e
                    break
            else:
                self.array[self.size] = e
            self.size += 1
        else:
            print("Overflow.")

    def intersect(self, A, B):
        for i in range(A.size):
            for j in range(B.size):
                if A.array[i] == B.array[j]:
                    self.insertElement(A.array[i])

    def union(self, A, B):
        for i in range(A.size):
            self.insertElement(A.array[i])
        for i in range(B.size):
            self.insertElement(B.array[i])

    def display(self):
        for i in range(self.size):
            print(self.array[i], end = ' ')
        print()

if __name__ == '__main__':
    SSet = Set()
    SSet.insertElement(4)
    SSet.insertElement(1)
    SSet.insertElement(3)
    SSet.insertElement(4)

    SSet.display()

    A = Set(); B = Set(); C = Set(); D = Set()
    L1 = [3, 5, 8, 5, 4, 9, 4, 7, 1]
    L2 = [6, 9, 5, 2, 3, 2, 1, 10]

    for e in L1:
        A.insertElement(e)
    for e in L2:
        B.insertElement(e)

    print('A : ', end=''); A.display()
    print('B : ', end=''); B.display()

    C.intersect(A, B); print('Intersect : ', end=''); C.display()
    D.union(A, B); print('Union : ', end=''); D.display()
