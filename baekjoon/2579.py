num = int(input())

stair = [0]
dp = []
for _ in range(num):
    stair.append(int(input()))

if num == 1:
    print(stair[0])
else:
    dp = [0] * (num+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    for i in range(3, num + 1):
        dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[num])

# https://daimhada.tistory.com/181
