import heapq
from sys import stdin

INF = int(1e9)
n,m,start = map(int,stdin.readline().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int,stdin.readline().split())
    graph[x].append((y,z))

print(graph)

def dijk(graph, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    print(distance)

dijk(graph,start)

cnt = 0
max_t = 0

for t in distance:
    if t != 1e9:
        cnt += 1
        max_t = max(max_t, t)

print(cnt-1, max_t)