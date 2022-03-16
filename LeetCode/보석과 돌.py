# 해시테이블로 풀이하기
import collections


def numStone(self, J:str, S:str):
    freqs = collections.defaultdict(int)
    count = 0

    for char in S:
        freqs[char] += 1

    for char in J:
        count += freqs[char]
    return count