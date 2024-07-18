# 두 배열의 원소 교체
import sys

input = sys.stdin.readline

n, k = map(int,input().split())

arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr.sort()
arr2 = sorted(arr2,reverse=True)
for i in range(k): 
    if arr[i] >= arr2[i]:
        break
    else:
        arr[i] = arr2[i]

print(sum(arr))