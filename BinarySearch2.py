import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))

start = 0 

result = 0

end = max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for x in arr:
        if mid < x:
            total += x-mid
    
    if total == m:
        result = mid
        break

    elif total < m:
        end = mid-1
    elif total > m:
        start = mid +1
    
    



print(result)







