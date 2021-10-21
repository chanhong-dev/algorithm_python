num = int(input())
temp = []

for i in range(num):
    x, y = list(map(int, input().split(' ')))
    # print(x, y)
    # temp.append([x, y])
    temp.append([y, x])
sort_num = sorted(temp)
# print(sort_num)

for j in range(num):
    print(sort_num[j][1], sort_num[j][0])
