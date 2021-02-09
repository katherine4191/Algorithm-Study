# ch5 BFS/DFS pratice problem

dpos = [(0,1), (1,0), (0,-1), (-1, 0)]
N, M = map(int, input().split())

ice_tray = [0 for _ in range(N)]
for i in range(N):
    ice_tray[i] = list(map(int, input()))

'''
ice_tray = [0 for _ in range(N)]
for i in range(N):
    ice_tray[i] = list(map(int, input()))
'''

def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if ice_tray[x][y] == 0:
        ice_tray[x][y] = 1

        for dx, dy in dpos:
            nx, ny = x + dx, y + dy
            dfs(nx, ny)
        return True
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            cnt += 1

print("output >>", cnt)

# 재귀함수에서 빠져나가는 조건을 정하기 어려웠는데, 항상 쓰던 조건이 있어서 당황스러웠다.
# C++ 때문에 main이 있는 것이 편해서 global 변수를 쓰면서 아등바등 구현했는데
# python은 그냥 맨 위에 선언했을 때 입력을 같이 받을 수 있어서 전역변수를 명시할 필요가 없었다는 것을 알게 되었다.

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

