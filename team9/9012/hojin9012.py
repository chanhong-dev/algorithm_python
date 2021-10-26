N = int(input())

def stack():
    words = list(input())
    a = []
    for j in words:
        if j == '(':
            a.append('(')
        else:
            if not a:
                return 'NO'
            a.pop()
    if a:
        return 'NO'
    else:
        return 'YES'


for i in range(N):
    print(stack())


