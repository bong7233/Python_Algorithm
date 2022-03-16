# 여기서 핵심은 처음 counter로 만든 해쉬형태의 키,벨류를 heap 에 반대로 넣는것이다.
# 우선순위 큐를 사용하는 heapq 모듈 사용
import collections
import heapq


def kFrequent(self, nums:[int], k:int):
    freqs = collections.Counter(nums)
    freqs_heap = []

    for f in freqs:
        heapq.heappush((freqs_heap), (-freqs[f],f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk