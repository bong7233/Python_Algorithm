# 온도리스트를 받아서 더 따뜻한 날까지 얼마나 기다려야하는지 리스트로 출력

def dT(T:[int]):
    # 입력리스트와 동일한 길이의 0리스트와 스택 생성
    result = [0] * len(T)
    stack = []

    # 입력리스트를 인덱싱을 달아서 반복문 실행
    for i, temp in enumerate(T):
        
        while stack and temp > T[stack[-1]]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)

    return result
