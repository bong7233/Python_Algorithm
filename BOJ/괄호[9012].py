n = int(input())

for i in range(n):
    vps_list = input()
    stack = []

    for vps in vps_list:
        if vps == "(":
            stack.append(vps)
        elif vps == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                stack.append(")")
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")