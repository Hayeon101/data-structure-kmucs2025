class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListType:
    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertFirst(self, data):
        node = Node(data)

        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node

        self.size += 1

    def insertLast(self, data):
        node = Node(data)

        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node

        self.size += 1

    def deleteFirst(self):
        if not self.isEmpty():
            p = self.tail
            q = p.next

            if p == q:
                self.tail = None
            else:
                p.next = q.next

            self.size -= 1
            return q.data
        else:
            print('Underflow.')

    def deleteLast(self):
        if not self.isEmpty():
            p = self.tail
            q = p.next

            if p == q:
                self.tail = None
            else:
                while q.next != p:
                    q = q.next

                self.tail = q
                q.next = p.next

            self.size -= 1
            return p.data
        else:
            print('Underflow.')

    def printList(self):
        p = self.tail

        if not self.isEmpty():
            while True:
                print('[%s] -> ' % (p.next.data), end = '')
                p = p.next

                # 시작 노드가 마지막 노드라면 끝내기
                if p == self.tail:
                    break

        print('\b\b\b    ')

if __name__ == '__main__':
    L = ListType()

    L.insertLast('C'); L.printList()
    L.insertFirst('A'); L.printList()
    L.insertFirst('B'); L.printList()
    L.insertLast('D'); L.printList()

    print('[%c] is deleted.' %L.deleteFirst()); L.printList()
