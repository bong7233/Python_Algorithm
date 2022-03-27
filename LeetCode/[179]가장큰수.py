class Solution:
    def largestNumber(self, li) -> str:
        for i in range(1,len(li)):  # 리스트의 1인덱스부터 시작
            while str(li[i]) + str(li[i-1]) > str(li[i-1]) + str(li[i]) and i > 0:
                # 현재인덱스와 바로 앞 인덱스의 숫자를 문자로바꿔서 합쳤을때 대소비교(i>0으로 범위벗어나지않게)
                li[i] , li[i-1] = li[i-1], li[i]
                i -= 1

        return str(int((''.join(map(str,li)))))