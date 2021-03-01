# 전보
# 도시 C에서 설치된 통로를 통해 최대한 많이 메시지를 전달(방향성 O)하며, 
# 도시 C에서 보낸 메시지를 받는 도시의 개수와 모두 메시지를 받는데 걸리는 시간을 구해야 하는 문제

import sys
import heapq
INF = int(1e9)

def dijkstra(graph, n_cnt, n_start):
    # 초기화
    dist = [INF] * (n_cnt + 1)
    que = []
    dist[n_start] = 0
    heapq.heappush(que, (0, n_start))

    while que:
        dist_a, now = heapq.heappop(que) # now, cost 순서 똑바로!
        if dist[now] < dist_a: # 갱신 여부 확인
            continue
        for b, cost in graph[now]:
            next_cost = dist_a + cost
            if next_cost < dist[b]:
                dist[b] = next_cost
                heapq.heappush(que, (dist[b], b)) 

    return dist


if __name__ == '__main__':
    input = sys.stdin.readline
    n, e, c = map(int, input().split())
    #graph = [[0] * (n + 1)] # => [[0, 0, 0, 0]]
    graph = [[] for _ in range(n + 1)] # => [[], [], [], []]
    
    for i in range(e):
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))

    dist = dijkstra(graph, n, c)
    dist.sort(reverse=True)
    print(dist[1])
    
'''
input
# n: city 개수, e: 통로 개수, c: 메시지를 보내고자 하는 city
# a b cost, cost: city a -> city b까지의 delivery time
3 2 1
1 2 4
1 3 2
'''