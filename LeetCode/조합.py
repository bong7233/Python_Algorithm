def combine(self, n, k):
    result = []

    def dfs(elements, start, k):
        # 백트레킹
        if k == 0:
            result.append(elements[:])
            return

        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)   # 순열과다르게 elements를 유지하며 재귀

            elements.pop()

    ## 본함수 시작 ##
    dfs([],1,k)
    return result