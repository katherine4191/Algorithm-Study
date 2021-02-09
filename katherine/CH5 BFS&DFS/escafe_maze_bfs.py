# ch5 BFS/DFS pratice problem

from collections import deque
dpos = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def BFS(x,y,r):
  global N, M, maze, visit
  visit[x][y]=1
  que = deque()
  que.append((x,y,r))
  while que:
      x,y,r = que.popleft()
      for dx,dy in dpos:
        nx, ny, nr = x + dx,y + dy, r+1
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visit[nx][ny]:
          continue
        if nx == N-1 and ny == M-1:
          return nr

        visit[nx][ny] = 1
        if maze[nx][ny] == 1:
          que.append((nx, ny, nr))

def __main__():
    global N, M, maze, visit

    N, M = map(int, input().split())
    maze = [0 for _ in range(N)]
    for i in range(N):
        maze[i] = list(map(int, input()))
    visit = [[0 for col in range(M)] for row in range(N)]

    return print("output >>", BFS(0, 0, 1))
  
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
