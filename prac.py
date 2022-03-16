from sys import stdin


n = input()

li = list(map(int,stdin.readline().split()))

print(max(li), min(li))

