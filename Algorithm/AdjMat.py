vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
visited = [False] * len(vName)

Graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

def printGraph():
    n = len(vName)
    print("    A  B  C  D  E  F  G  H")
    for i in range(n):
        print('%c |' % vName[i], end='')
        for j in range(n):
            print(' %d ' % Graph[i][j], end='')
        print(' |')

def rDfs(s):
    visited[s] = True
    print('[%s] ' % vName[s], end='')

    for t in range(len(vName)):
        if Graph[s][t] == 1 and visited[t] == False:
            rDfs(t)

if __name__ == '__main__':
    printGraph()
    print('\nrDFS : ', end='')
    rDfs(1)