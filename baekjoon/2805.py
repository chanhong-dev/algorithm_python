n, m = map(int, input().split(" "))

trees_height = list(map(int, input().split(" ")))

lt = 0
rt = max(trees_height)
min_height = 0

while lt <= rt:
    sum = 0
    mid = (lt + rt) // 2

    for i in trees_height:
        if i > mid:
            sum += (i - mid)

    if sum >= m:
        min_height = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(min_height)
