#개미 전사

import sys
input = sys.stdin.readline

n = int(input())

arr= list(map(int,input().split()))

#memoization

memoization = [0] * (n+1)

memoization[0] = arr[0]
memoization[1] = max(arr[0],arr[1])

for i in range(2,n):
    memoization[i] = max(memoization[i-1],memoization[i-2] + arr[i])
print(memoization[n-1])

