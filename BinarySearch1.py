import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

arr.sort()

m = int(input())

arrl = list(map(int,input().split()))


def binarySearch(start,end,target):
 mid = (start+end) // 2
 if start > end:
   return None
 elif arr[mid] == target:
  return mid
 if target > arr[mid]:
  return binarySearch(mid+1,end,target)
 elif target < arr[mid]:
  return binarySearch(start,mid-1,target)
    

for x in arrl:
 if binarySearch(0,len(arr)-1,x) == None:
  print('no', end = " ")
 else:
  print('yes', end = " ")
