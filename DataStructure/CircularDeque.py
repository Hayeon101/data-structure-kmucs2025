from CircularQueue import CircularQueue

class CircularDeque(CircularQueue):
    def __init__(self, capacity = 10):
        super().__init__(capacity)

    def addRear(self, e):
        self.enqueue(e)

    def deleteFront(self):
        self.dequeue()

    def getFront(self):
        self.peek()

    def addFront(self, e):
        if not self.isFull():
            self.array[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            print("Overflow.")

    def deleteRear(self):
        if not self.isEmpty():
            e = self.array[self.rear]
            self.rear = (self.rear - 1) % self.capacity
            return e
        else:
            print("Underflow.")

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            print("Underflow.")

if __name__ == '__main__':
    import random

    DQ = CircularDeque(10)

    for i in range(4):
        DQ.addFront(random.randint(65,90))
    DQ.display()

    for i in range(4):
        DQ.addRear(random.randint(65,90))
    DQ.display()

    for i in range(3):
        DQ.deleteRear()
    DQ.display()