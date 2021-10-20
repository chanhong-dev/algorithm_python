test_case = int(input())

for i in range(test_case):
    score_sum = 0
    count = 0
    students = list(map(int, input().split(' ')))

    num = students[0]
    for score in students[1:]:
        score_sum += score

    avg = score_sum/num

    for score in students[1:]:
        if score > avg:
            count += 1

    print('%.3f' % (count/num*100)+'%')
