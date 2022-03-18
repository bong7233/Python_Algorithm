def numCombination(self, digits):

    # 내포함수로 dfs 선언
    def dfs(index, path):
        # 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return

        # 쉽게 생각해서 각 문자를 돌면서 경우의수 모두 출력
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i+1, path+j)


    ### 본함수 시작부분 ###
    # 입력값이 없을떄 예외처리
    if not digits:
        return []

    # 자판 배열 입력
    dic = {"2":'abc',
           "3":'def',
           "4":'ghi',
           "5":'jkl',
           "6":'mno',
           "7":'pqrs',
           "8":'tuv',
           "9":'wxyz'}

    # 결과 담을 빈문자열 생성
    result = []

    # 초기 시작점을 0으로잡고 재귀시작
    dfs(0,"")

    return result
