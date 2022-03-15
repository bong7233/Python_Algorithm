from collections import deque

n=int(input())
q=deque(range(1,n+1))

while len(q)>1:
    q.popleft()
    q.append(q.popleft())
    # deque.rotate() 도 참고하면 좋다
print(q[0])