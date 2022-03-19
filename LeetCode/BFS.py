import collections

grahp = {}

# deque 이용해서 bfs 구현하기
def bfs(v):
    discovered = [v]
    dque = collections.deque(v)
    while dque:
        v = dque.popleft()
        for w in grahp[v]:
            if w not in discovered:
                discovered.append(w)
                dque.append(w)

    return discovered
