class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.array = [None] * capacity

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.capacity - 1

    def enqueue(self, e):
        if not self.isFull():
            self.rear += 1
            self.array[self.rear] = e
        else:
            print("Overflow.")

    def dequeue(self):
        if not self.isEmpty():
            self.front += 1
            return self.array[self.front]
        else:
            print("Underflow.")

    def display(self):
        print(f"Front : {self.front}, Rear : {self.rear}")
        print(self.array[self.front + 1:self.rear + 1])

if __name__ == '__main__':
    Q = ArrayQueue(10)

    data = ['A', 'B', 'C', 'D', 'E']

    for e in data:
        Q.enqueue(e)
    Q.display()

    print("Dequeue ==>", Q.dequeue())
    print("Dequeue ==>", Q.dequeue())
    Q.display()

    data = ['A', 'B', 'C', 'D', 'E']

    for e in data:
        Q.enqueue(e)
    Q.display()

    print("Dequeue ==>", Q.dequeue())
    print("Dequeue ==>", Q.dequeue())
    Q.display()

    Q.enqueue('F')
    Q.display()