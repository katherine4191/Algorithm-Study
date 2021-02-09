# ch5 BFS/DFS pratice problem

from collections import deque
dpos = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def __main__():
    N, M = map(int, input().split())

    ice_tray = [0 for _ in range(N)]
    for i in range(N):
        ice_tray[i] = list(map(int, input()))
    
    ''' another way
    ice_tray = []
    for i in range(N):
        ice_tray.append(list(map(int, input())))
    '''

    visit = [[0 for col in range(M)] for row in range(N)]
    cnt = 0
    que = deque()

    for i in range(N):
        for j in range(M):
            if visit[i][j] or ice_tray[i][j]:
                continue
            que.append((i, j))
            visit[i][j]=1
            cnt += 1
            while que:
                x, y = que.popleft()
                for dx,dy in dpos:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= M or visit[nx][ny]:
                        continue
                    visit[nx][ny] = 1

                    if ice_tray[nx][ny] == 0:
                      que.append((nx,ny))

    return  print("output >>", cnt) 

__main__()

'''
answer = 3
4 5 
00110
00011
11111
00000

answer = 8
5 7
1010101
0101010
1111000
0100111
0110000

answer = 1
4 5
10001
00000
00000
10001
'''

''' split 쓰면 큰일난다
  arr = [0 for _ in range(N)]
  for i in range(N):
    arr[i] = list(map(int, input().split()))
    # [[110], [11], [11111], [0]]
'''