def permute(self, nums:[]):
    result = []
    prev_elements = []
    
    def dfs(elements):
        # 백트래킹
        if len(elements) == 0:
            result.append(prev_elements[:])
        
        for e in elements:
            next_elements = elements[:]  # 원본 elements를 유지하기위해 copy
            next_elements.remove(e)      # 첫번쨰 요소를 뺌
            
            prev_elements.append(e)      # 뺀 요소를 prev에 저장
            dfs(next_elements)           # 재귀실행
                                         # 이때 재귀가 끝날때까지는 pop이 실행되지 않음
            prev_elements.pop()          # 마지막 재귀함수호출에서 prev를 result에 저장하면
                                         # for문의 다음 e를 위해 prev를 초기화
  
    ## 본함수 시작 ##
    
    dfs(nums)
    
    return result  # 각 단계에서 prev이 [1,2,3] 식으로 추가되었으므로
                   # result = [ [1,2,3], [1,3,2] ...] 이런식으로 나온다



# itertools 모듈사용하면 매우 단순하게 풀수있다
import itertools

def permute_itertools(self, nums:[]):
    return list(itertools.permutations(nums))
