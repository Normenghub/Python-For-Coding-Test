
dd=[[-1,0],[0,1],[1,0],[0,-1]]
n,m = map(int,input().split())

def outLine(v,h):
    return 0<= v <= n-1 and 0 <= h <= m-1
x,y,dUser = map(int,input().split())
def turnLeft(dUser):
   if dUser == 0:
      return 3
   else:
      return dUser - 1

maps = []
for _ in range(n):
 perHorizontalMap = list(map(int, input().split()))
 maps.append(perHorizontalMap)
count = 1
turn = 0
print(maps)
maps[x][y] = 1
while True:
   dUser = turnLeft(dUser)
   dv = x + dd[dUser][0]
   dh = y + dd[dUser][1]
   if outLine(dv,dh) and maps[dv][dh] == 0:
        maps[dv][dh] = 1
        count += 1
        x = dv
        y = dh
        turn = 0
        continue  

   else:
         turn +=1
   if turn == 4:
    dv = x - dd[dUser][0]
    dh = y - dd[dUser][1]
    if maps[dv][dh] == 1:
       break
    else:
       x= dv
       y = dh
       turn = 0
print(count)    
