a = input()
a = a.upper()
list_a = list(set(a))
max_count = []

for tmp in list_a:
    count = a.count(tmp)
    max_count.append(count)

if max_count.count(max(max_count)) > 1:
    print("?")

else:
    print(list_a[max_count.index(max(max_count))])
