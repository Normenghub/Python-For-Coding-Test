import sys
input = sys.stdin.readline

dp = [99999] * 30001
dp [1] = 0
for i in range(1,30001):
    if i * 5 <= 30000:
        dp[i*5] = min(dp[i*5] ,dp[i] + 1)
    if i * 3 <= 30000:    
     dp[i * 3] = min(dp[i*3] ,dp[i] + 1)
    if i + 1 <= 30000:
     dp[i+1] = min(dp[i+1] ,dp[i] + 1)
 


print(dp[int(input())])

#BottomUP DP