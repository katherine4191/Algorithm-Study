# ch5 BFS/DFS pratice problem

dpos = [(0,1),(1,0),(0,-1),(-1,0)]

def DFS(x, y):
    global N, M, ice_tray, visit
  
    for dx, dy in dpos:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M or visit[nx][ny] == 1:
            continue

        visit[nx][ny] = 1
        if ice_tray[nx][ny] == 0:
            DFS(nx, ny)


def __main__():
    global N, M, ice_tray, visit

    N, M = map(int, input().split())

    ice_tray = [0 for _ in range(N)]
    for row in range(N):
        ice_tray[row] = list(map(int, input()))

    visit = [[0 for _ in range(M)] for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if ice_tray[i][j] == 1 or visit[i][j] == 1:
                continue
            visit[i][j] = 1
            DFS(i,j)
            cnt += 1
    print("output >> ", cnt)
    return 0

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

for i in range(N):
    print(ice_tray[i],"  ",visit[i])
    print()
'''