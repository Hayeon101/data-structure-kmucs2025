import queue

Q = queue.Queue(maxsize=20)

for i in range(1,10):
    Q.put(i)

print('Queue : ', end = ' ')

for i in range(1,10):
    print(Q.get(), end=' ')
print()

S = queue.LifoQueue(maxsize=20)

for i in range(1,10):
    S.put(i)

print('Stack : ', end = ' ')

for i in range(1,10):
    print(S.get(), end=' ')