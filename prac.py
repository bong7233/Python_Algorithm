def isValid(s) -> bool:
    s = list(s)
    while len(s) > 1:
        if s.pop(0) != s.pop():
            print("x")
            break
        else:
            s.pop()
            s.pop(0)
    print("O")

isValid("{()}")