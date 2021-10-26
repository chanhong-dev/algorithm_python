N, M = map(int, input().split())
arr = list(map(int, input().split()))

a = 1
b = max(arr)

while a <= b:
    sum_r = 0
    guess = (a + b) // 2
    for ar in arr:
        if ar - guess > 0:
            sum_r += ar - guess
    if sum_r >= M:
        a = guess + 1
    else:
        b = guess - 1

print(b)
