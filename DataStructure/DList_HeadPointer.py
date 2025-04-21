class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DListType:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.head.next = self.tail
        # self.tail.prev = self.head
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertFirst(self, data):
        node = Node(data, next=self.head)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.head.prev = node
            self.head = node

        self.size += 1

    def insertLast(self, data):
        node = Node(data, prev=self.tail)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def printList(self):
        p = self.head

        while p:
            print("[%s] <=> " % p.data, end='')
            p = p.next
        print("\b\b\b\b     ")

if __name__ == '__main__':
    DL = DListType()

    DL.insertLast('A'); DL.printList()
    DL.insertFirst('B'); DL.printList()
    DL.insertFirst('C'); DL.printList()
    DL.insertLast('D'); DL.printList()
