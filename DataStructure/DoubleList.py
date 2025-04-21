class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DListType:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insert(self, pos, data):
        if pos <= 0 or pos > self.size + 1:
            print("Invalid Pos.")
            return

        p = self.head

        for _ in range(1,pos):
            p = p.next

        node = Node(data)
        node.prev = p
        node.next = p.next
        p.next.prev = node
        p.next = node

        self.size += 1

    def delete(self,pos):
        if pos <= 0 or pos > self.size:
            print("Invalid Pos.")
            return

        p = self.head

        for _ in range(pos):
            p = p.next

        data = p.data

        p.prev.next = p.next
        p.next.prev = p.prev

        self.size -= 1

        return data

    def printList(self):
        p = self.head.next


        while p != self.tail:
            print("[%s] <=> " % p.data, end='')
            p = p.next
        print("\b\b\b\b     ")

if __name__ == '__main__':
    DL = DListType()

    DL.insert(1, 'A'); DL.printList()
    DL.insert(1, 'B'); DL.printList()
    DL.insert(2, 'C'); DL.printList()
    DL.insert(4, 'D'); DL.printList()

    print("[%s] is deleted." %DL.delete(1)); DL.printList()