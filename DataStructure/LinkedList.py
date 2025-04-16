class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class ListType:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None
        #return self.size == 0

    def insertFirst(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size += 1

    def getNode(self, pos):
        p = self.head

        for _ in range(1,pos-1):
            p = p.next

        return p

    def insert(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
        else:
            if pos <= self.size + 1:
                p = self.getNode(pos)

                node = Node(data, p.next)
                p.next = node
                self.size += 1
            else:
                print("Invalid Position")

    def deleteFirst(self):
        if not self.isEmpty():
            p = self.head
            self.head = p.next
            self.size -= 1
            return p.data
        else:
            print('Underflow.')

    def delete(self, pos):
        if pos <= 0 or pos > self.size:
            print('Invalid Pos.')
            return

        if not self.isEmpty():
            if pos == 1:
                return self.deleteFirst()
            else:
                q = self.getNode(pos)
                p = q.next

                q.next = p.next
                self.size -= 1

                return p.data
        else:
            print('Underflow.')

    def printList(self):
        p = self.head

        while p != None:
            print('[%s] -> ' % (p.data), end='')
            p = p.next

        print('\b\b\b    ')

if __name__ == '__main__':
    L = ListType()

    L.insertFirst('A'); L.printList()
    L.insertFirst('B'); L.printList()

    L.insert(2,'C'); L.printList()
    L.insert(3,'D'); L.printList()
    L.insert(2,'E'); L.printList()

    print('[%c] is deleted.' % L.deleteFirst()); L.printList()
    print('[%c] is deleted.' % L.delete(3)); L.printList()