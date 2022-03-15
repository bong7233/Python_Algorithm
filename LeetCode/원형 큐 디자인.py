# 원형 큐는 링 버퍼 라고도 불린다
# FIFO 구조를 지니고 마지막위치기 시작위치와 연결되는 큐

class CircularQueue:
    def __init__(self, k:int):
        self.q = [None]*k
        self.maxlen = k
        self.p1 =0
        self.p2 =0

    def enQueue(self, value:int):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2+1)% self.maxlen # 포인터가 최다값 벗어나지않게
            return True
        else:
            return False

    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 +1) % self.maxlen
            return True

    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        return -1 if self.q[self.p2 -1] is None else self.q[self.p2 -1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None