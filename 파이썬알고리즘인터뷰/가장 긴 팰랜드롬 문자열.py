# 팰린드롬 구현
def longPalindrome(s: str) -> str:
    # 투포인터 구현
    def expand(left: int, right: int) -> str:
        # 두개의 포인터가 범위내에있고, 양끝이 같은문자를 나타내는지(대칭인지)확인
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 대칭이 계속 유지된다면, 양끝의 위치를 한칸씩 넓힘
            left -= 1
            right += 1
        # 대칭되는 양 끝단의 위치를 찾아서 슬라이싱후 리턴
        return s[left + 1:right]

    # 만약 문자열이 한글자이거나 이미 거꾸로해도 같은상황이라면 바로 문자열 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i + 1), # 두칸짜리 투포인터(짝수 반복구간 찾기)
                     expand(i, i + 2), # 세칸짜리 투포인터(홀수 반복구간 찾기)
                     key=len)          # 길이를 기준
    return result

## 테스트
print(longPalindrome('abcaabbaasda')) # aabbaa
print(longPalindrome('awwbwwc'))      # wwbww