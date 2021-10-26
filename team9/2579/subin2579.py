t = int(input())

num = []
dp = []

for i in range(t):
    num.append(int(input()))

if t == 1:
    print(num[0])
    exit()
if t == 2:
    print(num[0] + num[1])
    exit()

dp.append(num[0])
dp.append(dp[0] + num[1])
dp.append(max(num[0] + num[2], num[1] + num[2]))

for n in range(3, t):
    dp.append(max(num[n] + num[n - 1] + dp[n - 3], num[n] + dp[n - 2]))

print(dp[-1])
