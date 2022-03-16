# 파이썬의 딕셔너리는 오픈어드레싱을 사용하고있음
# 이 문제는 개별 체이닝 방식으로 구현

import collections
from linkedList import ListNode


class HashMap:
    def __init__(self):
        self.size = 100
        self.table = collections.defaultdict()

    def put(self, key:int, value:int):
        idx = key% self.size    # 해시함수 기능
        if self.table[idx].value is None:
            #  .value 넣는 이유는 collectionsdict가 자동으로 default key를 생성하여 집어넣기떄문에
            # table[idx] is None: 으로 돌리면 table[idx] 는 절대 None이 되지않는다(if문 무쓸모해짐)
            self.table[idx] = ListNode(key,value)
        return

        p = self.table[idx]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key:int):
        idx = key % self.size
        if self.table[idx].value is None:
            return -1

        p = self.table[idx]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key:int):
        idx = key % self.size
        if self.table[idx].value is None:
            return

        p = self.table[idx]
        if p.key == key:
            self.table[idx] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key==key:
                prev.next = p.next
                return
            prev,p=p,p.next

