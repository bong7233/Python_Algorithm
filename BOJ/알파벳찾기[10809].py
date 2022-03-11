import string

word = input()
# 알파벳수(26개)의 -1 로 채워진 리스트 생성
result = [-1]*len(string.ascii_lowercase) # [-1, -1, -1,..., -1]
# 입력값인 str을 기준으로 반복문 실행
for i in range(len(word)):
    idx = ord(word[i]) - 97  # 아스키코드 ord('a')가 97인것을 이용하여 result 내부 인덱스 설정
    if result[idx] == -1:
        result[idx] = i

# 리스트형태의 값 join으로 바꿔서 출력
print(' '.join([str(num) for num in result]))
