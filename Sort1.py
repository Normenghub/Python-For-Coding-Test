# 위에서 아래로
arr = []

for i in range(int(input())): arr.append(int(input()))

arr = sorted(arr,reverse=True)

for i in range(len(arr)): print(arr[i])