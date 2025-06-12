INF = 1000

vName = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Graph = [
        [ 0, 7, INF, INF, 3, 10, INF],
        [ 7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 0, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [ 3, 2, INF, 11, 0, 13, 5],
        [ 10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0]
]

def printGraph():
    n = len(vName)
    print("     A   B   C   D   E   F   G")
    for i in range(n):
        print ("%c |" % vName [i], end='')
        for j in range(n):
            if Graph[i][j] == INF:
                print(' * ', end='')
            else:
                print ("%3d " % Graph[i][j], end='')
        print(" |")
    print()

def floyd():
    n = len(vName)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if Graph[i][j] > Graph[i][k] + Graph[k][j]:
                    Graph[i][j] = Graph[i][k] + Graph[k][j]

        print('k = %d' % k)
        printGraph()

if __name__ == '__main__':
    floyd()