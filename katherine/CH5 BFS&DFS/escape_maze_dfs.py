# ch5 BFS/DFS pratice problem

dpos = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def DFS(x,y,cnt):
  global N, M, mincnt
  if x == N-1 and y == M-1:
    if mincnt > cnt:
      mincnt = cnt
    return cnt

  for dx, dy in dpos:
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= N or y < 0 or ny >= M or arr[nx][ny] == 0 or visit[nx][ny] == 1:
      continue
    
    if arr[nx][ny] == 1:
      visit[nx][ny] = 1
      DFS(nx, ny, cnt+1)
      visit[nx][ny] = 0

def __main__():
    global N, M, mincnt, arr, visit

    N, M = map(int, input().split())
    mincnt = 201 * 201
    arr = []
    for i in range(N):
        arr.append(list(map(int, input())))

    visit = [[0 for col in range(M)] for row in range(N)]
    visit[0][0] = 1

    DFS(0, 0, 1)

    return print("output >>", mincnt)
  
__main__()

''' 
answer = 10
5 6
101010
111111
000001
111111
111111

answer = 20
5 10 
1001100011
1001110100
1111010111
1010010101
1110111101
'''