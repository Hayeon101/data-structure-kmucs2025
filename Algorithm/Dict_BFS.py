Graph = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','D','E'],
    'D':['B','C','F'],
    'E':['C','G','H'],
    'F':['D'],
    'G':['E','H'],
    'H':['E','G']
}

visited = {}

from queue import Queue

def BFS(s):
    Q = Queue()

    Q.put(s)
    visited[s] = True # 'D':True
    print('[%c] ' %s, end='')

    while not Q.empty():

        s = Q.get()

        for t in Graph[s]:
            if t not in visited:
                Q.put(t)
                visited[t] = True
                print('[%c] ' %t, end='')


if __name__ == '__main__':
    print('BFS : ', end='')
    BFS('D')