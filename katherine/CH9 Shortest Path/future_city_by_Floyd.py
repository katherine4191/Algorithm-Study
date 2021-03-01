# ch 9. 미래 도시
# 방문 판매원 1번 회사 -> k번 회사 -> X번 회사
# 방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 구하시오

INF = int(1e9) # 무한을 의미하는 값

def Floyd_Warshall(n, e):
    dist = [[INF] * (n + 1) for a in range(n + 1)]

    # 대각 행렬 및 간선 정보 초기화
    for a in range(1, n + 1):
        dist[a][a] = 0

    for _ in range(e):
        a, b = map(int, input().split())
        dist[a][b], dist[b][a] = 1, 1
    
    for l in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # 노드 k를 거쳐가지 않을 때 거리와 노드 l를 거쳐서 갈 때의 거리 
                dist[a][b] = min(dist[a][b], dist[a][l] + dist[l][b])
    return dist

if __name__ == '__main__':
    n, e = map(int, input().split())
    dist = Floyd_Warshall(n, e)
    
    x, k = map(int, input().split())
    answer = dist[1][k] + dist[k][x]
    if answer >= INF:
        print(-1)
    else:
        print(answer)

'''
input 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
output 1: 3

input 2
4 2
1 3
2 4
3 4
output 2: -1
'''