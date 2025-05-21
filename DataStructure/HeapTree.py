N = 20

class MaxHeap:
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0

    def upHeap(self):
        i = self.heapSize
        key = self.heap[i]

        while (i != 1) and (key > self.heap[i // 2]):
            self.heap[i] = self.heap[i // 2]
            i //= 2

        self.heap[i] = key

    def insertItem(self, item):
        self.heapSize += 1    # 0번째 칸에는 넣지 않음
        self.heap[self.heapSize] = item
        self.upHeap()

    def downHeap(self):
        p = 1
        c = 2
        key = self.heap[p]

        while c <= self.heapSize:
            if (c < self.heapSize) and (self.heap[c+1] > self.heap[c]):  # 오른쪽 자식이 왼쪽 자식보다 크다면
                c += 1  # 현재 자식을 오른쪽 자식으로 바꿈

            if key >= self.heap[c]:   # 자식보다 이미 크거나 같으면 끝
                break

            self.heap[p] = self.heap[c]
            p = c  # 자식이 됨
            c *= 2   # 손주가 됨

        self.heap[p] = key

    def deleteItem(self):
        key = self.heap[1]
        self.heap[1] = self.heap[self.heapSize]
        self.heapSize -= 1
        self.downHeap()

        return key


if __name__ == '__main__':
    H = MaxHeap()
    data = [9,7,6,5,4,3,2,2,1,3]

    for e in data:
        H.insertItem(e)
        print('Heap :', H.heap[1:H.heapSize + 1])

    H.insertItem(8)
    print('Heap :', H.heap[1:H.heapSize + 1])
    print()

    print('[%d] is deleted.' % H.deleteItem())
    print('Heap :', H.heap[1:H.heapSize + 1])
    print()