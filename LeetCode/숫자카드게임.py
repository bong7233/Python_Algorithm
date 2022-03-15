# 행렬을 이용한 그리디연습
# 단순 행렬연습
# row만큼의 행이있는 2중리스트에서
# 각 행의 최소값을 찾은뒤 최소값들 중 최대값을 찾기
def game(li,row):
    for i in range(row):
        li[i] = min(li[i])
    print(max(li))

li = [
    [3,1,2],
    [4,1,4],
    [2,2,2]
]

game(li,3)  # 2