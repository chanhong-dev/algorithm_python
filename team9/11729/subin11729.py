t = int(input())
cnt = 2 ** t - 1



def hanoi(t, start, end, mid):
    if t == 1:
        print(start, end)
        return
    hanoi(t - 1, start, mid, end)
    print(start, end)
    hanoi(t - 1, mid, end, start)

print(cnt)
hanoi(t, 1, 3, 2)
