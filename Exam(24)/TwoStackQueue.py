import queue

class QueueByStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.main_stack = queue.LifoQueue(maxsize=self.capacity)
        self.temp_stack = queue.LifoQueue(maxsize=self.capacity)

    def enqueue(self, e):
        if not self.main_stack.full():
            self.main_stack.put(e)
            self.size += 1
        else:
            print("Overflow.")

    def dequeue(self):
        if not self.main_stack.empty():
            while self.size > 1:
                self.temp_stack.put(self.main_stack.get())
                self.size -= 1
            item = self.main_stack.get()
            self.size -= 1
            while not self.temp_stack.empty():
                self.main_stack.put(self.temp_stack.get())
                self.size += 1
            return item
        else:
            print("Underflow.")

if __name__ == '__main__':
    Queue = QueueByStack(20)
    Queue.enqueue(1)
    Queue.enqueue(2)
    print(Queue.dequeue())
    Queue.enqueue(3)
    print(Queue.dequeue())
    print(Queue.dequeue())
