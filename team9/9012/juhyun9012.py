T = int(input())


def solution(str):
    stack = []
    for v in str:
        if v == '(':
            stack.append(v)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    else:
        if len(stack) != 0:
            return False
        else:
            return True


for i in range(T):
    inputs = input()
    if solution(inputs):
        print("YES")
    else:
        print("NO")