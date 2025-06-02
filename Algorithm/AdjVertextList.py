vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
visited = [False] * len(vName)

AdjVer = [
    [1, 2],
    [0, 3],
    [0, 3, 4],
    [1, 2, 5],
    [2, 6, 7],
    [3],
    [4, 7],
    [4, 7]
]

from queue import LifoQueue

class Stack(LifoQueue):
    def peek(self):
        if not self.empty():
            return self.queue[-1]
        raise Exception("Stack is Empty")

def iDfs(s):
    S = Stack()

    S.put(s)
    visited[s] = True
    print('[%s] ' % vName[s], end='')

    while not S.empty():
        s = S.peek()
        flag = False

        for t in AdjVer[s]:
            if visited[t] == False:
                S.put(t)
                visited[t] = True
                print('[%s] ' % vName[t], end='')

                flag = True
                break

        if flag == False:
            S.get()

if __name__ == '__main__':
    print('iDFS : ', end='')
    iDfs(1)