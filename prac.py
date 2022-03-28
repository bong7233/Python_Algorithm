from sys import stdin

'''
백준[10825] 국영수 
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

문제 시간제한 : 1초
파이썬 : 1초에 약 2천만번 계산 가능

문제의 n 범위 : 최대 10만
-> 퀵 정렬 : O(n^2) = 10만 x 10만 = 억단위
-> 퀵정렬 불가능

내장함수인 sort 사용 O(nlogn)
'''

# input 입력
n = int(stdin.readline())
students = []
for _ in range(n):
    student = list(stdin.readline().split())
    students.append(student)


# 왜 역순으로 작동하는지? Tim Sort?
students.sort(key=lambda student: student[0])                       # 이름 오름차순
students.sort(key=lambda student: int(student[3]), reverse=True)    # 수학 내림차순
students.sort(key=lambda student: int(student[2]))                  # 영어 오름차순
students.sort(key=lambda student: int(student[1]), reverse=True)    # 국어 내림차순


# 튜플에 우선순위가 높은 조건 순서대로 넣으면 key에서 자동으로 적용
# 정렬 우선순위(국어->영어->수학->이름)
# 오름차순은 음수처리로 간단하게 해결
students.sort(key=lambda student: (-int(student[1]), # 국어
                                   int(student[2]),  # 영어
                                   -int(student[3]), # 수학
                                   student[0]))      # 이름

for student in students:
    print(student[0])