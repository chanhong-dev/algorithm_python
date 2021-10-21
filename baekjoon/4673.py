num = set(range(1, 10000))

rm = set()

for n in num:
    for m in str(n):
        n += int(m)

    rm.add(n)

num = num - rm

for k in sorted(num):
    print(k)
