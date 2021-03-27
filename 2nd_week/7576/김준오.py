from collections import deque
import sys

need_check_list = deque()
tomato_check = False

dx = [1,0,-1,0]
dy = [0,-1,0,1]
max_day = 0

M,N = map(int,input().split())
background = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

for i in range(N):
  for j in range(M):
    if background[i][j] == 1:
      need_check_list.append((i,j))

while need_check_list:
  x,y = need_check_list.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M :
      if background[nx][ny] == 0:
        background[nx][ny] = background[x][y]+1
        max_day = max(background[nx][ny],max_day)
        need_check_list.append((nx,ny))

for i in range(N):
  if 0 in background[i]:
    print(-1)
    exit()

if max_day == 0:
  print(0)
else :
  print(max_day-1)
