n, m = map(int, input().split(" "))

trees_height = list(map(int, input().split(" ")))

sum = 0
lt = 0
rt = max(trees_height)
min_height = 0
while lt <= rt:
    mid = (lt + rt) // 2

    for i in trees_height:
        sum += i - mid

    if sum < m:
        min_height = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(min_height)

# https://www.acmicpc.net/blog/view/109