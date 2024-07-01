# 음료수 얼려 먹기
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
dd= [[1,0],[-1,0],[0,1],[0,-1]]
graph = []
trueFalse = []
queue = deque()
for i in range(n):
    v = list(input().rstrip())
    c = []
    for k in range(len(v)):
        c.append(False)
        if v[k] == '0':
            queue.append([i,k])
        else:
            continue
    graph.append(v)
    trueFalse.append(c)
def toGo(d,c):
    return 0 <= d <= n-1 and 0 <=c<=m-1
count = 0
def dfs(d,c,trueFalse,graph):
    trueFalse[d][c] = True
    for dr,dc in dd:
        ddr = d+dr
        ddc = c+dc
        if toGo(ddr,ddc):
         if not trueFalse[ddr][ddc] and graph[ddr][ddc] == '0':
            dfs(ddr,ddc,trueFalse,graph)
while queue:
    v = queue.popleft()
    if trueFalse[v[0]][v[1]] == True:
        continue
    else:
        count+=1
        dfs(v[0],v[1],trueFalse,graph)
print(count)
        


