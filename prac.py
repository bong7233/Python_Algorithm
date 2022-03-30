n = int(input())
lst = list(map(int,input().split()))
list_rank = list(sorted(set(lst)))

dic = {list_rank[i]:i for i in range(len(list_rank))}

for i in lst:
    print(dic[i], end=' ')