from DataStructure.CircularQueue import CircularQueue

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPos(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    return False

def BFS():
    Q = CircularQueue()
    Q.enqueue((1, 0))
    print("BFS : ")

    while not Q.isEmpty():
        pos = Q.dequeue()
        (r, c) = pos
        print(pos, end=' -> ')

        if (map[r][c] == 'x'):
            return True
        else:
            map[r][c] = '.'
            if isValidPos(r-1, c): Q.enqueue((r-1, c))
            if isValidPos(r+1, c): Q.enqueue((r+1, c))
            if isValidPos(r, c-1): Q.enqueue((r, c-1))
            if isValidPos(r, c+1): Q.enqueue((r, c+1))

        if Q.front < Q.rear:
            print(Q.array[Q.front+1:Q.rear+1])
        else:
            print(Q.array[Q.front + 1:Q.capacity] + Q.array[0:Q.rear + 1])

    return False

if __name__ == '__main__':
    result = BFS()

    if result:
        print('Success')
    else:
        print('Fail')