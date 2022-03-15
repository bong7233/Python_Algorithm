# 정렬시킨 후 두개씩 묶을때 짝수번쨰 위치(0,2,4...)에는 항상 작은값이 온다
# 그러므로 정렬후 짝수번쨰 요소들 == min(짝,홀) 이다

# 배열파티션 구현
def arrayPairSum(nums:[int]) -> int:
    return sum(sorted(nums)[::2])

# 테스트
nums = [1,4,3,2,5,9]
print(arrayPairSum(nums)) # 9