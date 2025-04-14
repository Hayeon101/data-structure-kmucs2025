class CircularQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = [None] * capacity

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = e
        else:
            print("Overflow.")

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("Underflow.")

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            print("Underflow.")

    def display(self):
        print(f"Front : {self.front}, Rear : {self.rear}")
        i = self.front

        while i != self.rear:
            i = (i + 1) % self.capacity
            print("[%c] " % self.array[i], end="")
        print()

if __name__ == '__main__':
    Q = CircularQueue(10)

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