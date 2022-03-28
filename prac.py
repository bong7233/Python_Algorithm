from sys import stdin

'''
문제의 n 범위가 최대 10만
퀵 정렬을 사용하면 최악의 경우(O(n^2) = 억단위 계산

파이썬은 1초에 약 2천만번의 계산이 가능하므로 퀵정렬 불가능
내장함수인 sort 사용 O(nlogn)
'''


n = int(stdin.readline())
students = []
for _ in range(n):
    student = list(stdin.readline().split())
    students.append(student)

# 이런식의 코드도 가능하지만 왜 역순으로 작동하는지는? Tim Sort의 메커니즘때문이 아닐까?
# students.sort(key=lambda student: student[0])                       # 이름 오름차순
# students.sort(key=lambda student: int(student[3]), reverse=True)    # 수학 내림차순
# students.sort(key=lambda student: int(student[2]))                  # 영어 오름차순
# students.sort(key=lambda student: int(student[1]), reverse=True)    # 국어 내림차순


# 튜플에 우선순위가 높은 조건 순서대로 넣으면 key에서 자동으로 적용
# 정렬 우선순위(국어->영어->수학->이름)
# 오름차순은 음수처리로 간단하게 해결
students.sort(key=lambda student: (-int(student[1]), # 국어
                                   int(student[2]),  # 영어
                                   -int(student[3]), # 수학
                                   student[0]))      # 이름

for student in students:
    print(student[0])