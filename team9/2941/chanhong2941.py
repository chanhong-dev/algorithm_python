a = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for temp in croatia:
    if temp in a:
        # count += 1
        # print(temp, count)
        a = a.replace(temp, ' ')

print(len(a))
