# 슬라이딩윈도우 + 투포인터
# 포인터 두개모두 0에서 출발하여 하나만 확장
# 중복문자가 나오기전까지 하나만 계속 확장
# 중복나오면 출발지점의 포인터를 확장하던위치로 이동 -> 반복
# 포인터 두개사이의 길이가 최대가될떄 크기 고정후 이동(슬라이딩윈도우)

def longString(self, s: str):
    used = {}
    max_len = start = 0
    for idx, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_len = max(max_len, idx-start+1)

        used[char] = idx
    return max_len

