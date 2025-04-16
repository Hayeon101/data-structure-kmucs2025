class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class StackType:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        node = Node(data, self.top)
        self.top = node
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            p = self.top
            self.top = p.next
            self.size -= 1
            return p.data
        else:
            print("Underflow")


    def printList(self):
        p = self.top

        while p != None:
            print('[%s] <- ' % (p.data), end='')
            p = p.next

        print('\b\b\b    ')

if __name__ == '__main__':
    S = StackType()

    S.push('A'); S.printList()
    S.push('B'); S.printList()
    S.push('C'); S.printList()
