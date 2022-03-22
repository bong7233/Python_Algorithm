class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for i in tokenList:
        # 연산자이면서 Stack 이 비어있을 때
        if i in prec and opStack.isEmpty():
            opStack.push(i)

        # 여는 괄호일 때 push
        elif i == '(':
            opStack.push(i)

        elif i in prec:

            # 연산자이면서 top 의 우선순위가 낮을 때 까지 pop
            while not opStack.isEmpty():

                if prec[opStack.peek()] >= prec[i]:
                    postfixList.append(opStack.pop())
                else:
                    break
            opStack.push(i)

        # 닫는 괄호일 때 여는 괄호를 만날 때 까지 pop
        elif i == ')':
            while True:
                t = opStack.pop()
                if t == '(' or opStack.isEmpty():
                    break
                postfixList.append(t)
        # 피연산자가 아닐 경우
        else:
            postfixList.append(i)

        # 끝에 왔을 때 Stack에 남아있는 것 출력
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    pass


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val