str = input()
check=["c=","c-","dz=","d-","lj","nj","s=","z="]
count = 0
while True:
    for v in check:
        if v in str:
            str = str.replace(v, "x",1)
            count += 1
            break;
    else:
        break;
for v in str:
    if v !="x":
        count+=1
print(count)