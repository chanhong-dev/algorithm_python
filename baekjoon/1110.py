num = int(input())
temp = num
count = 0


while True:
    units = num % 10
    tens = num // 10
    num_sum = tens + units
    num = (units * 10) + (num_sum % 10)

    count += 1

    if temp == num:
        print(count)
        break
