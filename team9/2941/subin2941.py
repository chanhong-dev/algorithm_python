strr = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in range(len(croatia)):
    if croatia[i] in strr:
        cnt += 1
        strr = strr.replace(croatia[i], "/")

print(len(strr))
