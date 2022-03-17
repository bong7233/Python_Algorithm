import collections

progress = [55,30,93]
speed = [5,30,1]

suc = list(zip(progress,speed))
# print(suc)

n = 1
dic = collections.defaultdict(int)
# print(dic)
while len(suc) != 0:
    count = 0
    if suc[-1][0] + suc[-1][1]*n >= 100:
        suc.pop()
        count += 1
        dic[n] += 1
    else:
        n += 1

print(list(dic.values()))