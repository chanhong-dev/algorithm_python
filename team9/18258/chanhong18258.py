import sys
from collections import deque

num = int(input())
deq = deque()
for _ in range(num):
    # cmd = list(map(str, input().split(" ")))
    cmd = sys.stdin.readline().split()
    # print(cmd)

    if cmd[0] == 'push':
        deq.append(cmd[1])
    elif cmd[0] == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print("-1")
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    elif cmd[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print("-1")
    elif cmd[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print("-1")
