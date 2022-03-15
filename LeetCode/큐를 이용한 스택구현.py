import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque

    def push(self,value):
        self.q.append(value)

        for _ in range(len(self.q) -1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q)==0