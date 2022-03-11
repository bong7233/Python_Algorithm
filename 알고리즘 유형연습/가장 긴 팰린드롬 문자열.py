# 가장 긴 팰린드롬 문자열 찾기
# 팰린드롬이란, 좌우가 대칭되는 문자
# 이번 문제는 입력받은 문자열 내에서 가장 긴 펠린드롬 문자를 찾는것

def longPalindrome(s: str) -> str:
    # 투포인터 구현함수 구현
    def twoPointer(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 대칭이 계속 유지된다면, 양끝의 위치를 한칸씩 넓힘
            left -= 1
            right += 1
        return s[(left + 1): right]


    # 만약 문자열이 한 글자 or 이미 팰린드롬이라면 그대로 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result,
                     twoPointer(i, i + 1),  # 두칸짜리 투포인터
                     twoPointer(i, i + 2),  # 세칸짜리 투포인터
                     key=len)
    return result

# 테스트
print(longPalindrome('awwbwwc'))  # wwbww