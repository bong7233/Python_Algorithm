from collections import deque
from sys import stdin

num = int(stdin.readline())
for _ in range(num):
    N, M = map(int,stdin.readline().split())
    que = deque(map(int,stdin.readline().split()))
    cnt = 0
    while que:
        top = max(que)
        M -= 1
        pop = que.popleft()
        if top != pop:
            que.append(pop)
            if M < 0:
                M = len(que)-1
        else:
            cnt+=1
            if M == -1:
                print(cnt)
                break