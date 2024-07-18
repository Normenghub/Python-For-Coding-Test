# 성적이 낮은 순서로 학생 출력하기

arr= []

for i in range(int(input())): arr.append(list(map(str,input().split())))

arr = sorted(arr,key=lambda x : x[1])

for i in range(len(arr)): print(arr[i][0],end =" ")