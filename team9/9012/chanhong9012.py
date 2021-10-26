count = int(input())

for i in range(count):
    brackets = input()
    brackets_list = list(brackets)
    temp = 0

    # print(bracket_list)
    for bracket in brackets_list:
        if bracket == '(':
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            break

    if temp == 0:
        print("YES")
    else:
        print("NO")
