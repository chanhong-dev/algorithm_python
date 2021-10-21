count = int(input())
tmp = 0
for i in range(count):
    word = input()
    for w in range(len(word)):
        if w < len(word)-1:
            if word[w] == word[w+1]:
                pass
            elif word[w] in word[w+1:]:
                break
        else:
            tmp += 1

print(tmp)