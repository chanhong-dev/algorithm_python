m = int(input())

print(2**m-1)


def hanoi(n, p1, p2, p3):
    if n == 1:
        print(p1, p3)
    else:
        hanoi(n-1, p1, p3, p2)
        print(p1, p3)
        hanoi(n-1, p2, p1, p3)


hanoi(m, 1, 2, 3)

# https://www.youtube.com/watch?v=FYCGV6F1NuY
# https://jwmath.tistory.com/103