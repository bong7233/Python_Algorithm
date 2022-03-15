# 코드의 핵심은 2개의 stack을 사용한다는것
# pop()을 호출할때 peek()도 호출

class MyQueue:
    def __init__(self):
        self.input =[]
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []