"""
간단한 다익스트라 알고리즘
0. 방문하지 않는 노드 중 최단 거리의 노드를 현재 노드로 삼는다.
1. 현재 노드와 연결된 노드로의 거리를 계산한다.
2. [현재노드까지의 최단거리 (최단거리 테이블에서 찾는다) + 연결 노드로의 거리 < 최단거리 상 연결노드로의 거리] 일 때 최단거리 테이블을 갱신한다.
3. 모든 노드를 방문할 때 까지 위 알고리즘을 반복한다.
"""

def dijkstra(adjacency_list, start):
    min_distance_list = [float('inf') for _ in range(len(adjacency_list))] # 모든 노드로의 거리를 무한대로 초기화
    min_distance_list[start] = 0 # 시작점까지의 최소거리는 항상 0
    not_visited = set(range(len(adjacency_list)))
    not_visited.remove(0)

    # 아직 방문하지 않은 노드가 남아있다면
    while not_visited:
        not_visited.remove(start)

        # 최단 거리의 노드 찾고
        destinations = sorted(adjacency_list[start], key=lambda x: x[1])
        start_before = start  # 이전 지점을 기억
        for candidate, _ in destinations:
            if candidate in not_visited: # 방문하지 않은 노드 중에서 최단 거리 노드를 찾기
                start = candidate  # 최단 거리의 노드를 다음 반복의 새로운 시작점으로 갱신
                break
        else:
            break

        # 연결 노드의 최단 거리 갱신
        for destination, cost in destinations:
            if min_distance_list[destination] > min_distance_list[start_before] + cost:
                min_distance_list[destination] = min_distance_list[start_before] + cost

    return min_distance_list


if __name__ == "__main__":
    # node_counts, edge_counts = map(int, input().split())
    # starting_point = int(input())
    # adjacency_list = [[] for _ in range(node_counts + 1)]
    # for _ in range(edge_counts):
    #     source, destination, cost = map(int, input().split())
    #     adjacency_list[source].append((destination, cost))

    starting_point = 1
    adjacency_list = [
        [],
        [(2, 2), (3, 5), (4, 1)],
        [(3, 3), (4, 2)],
        [(2, 3), (6, 5)],
        [(3, 3), (5, 1)],
        [(3, 1), (6, 2)],
        []
    ]

    result = dijkstra(adjacency_list=adjacency_list, start=starting_point)

    for i in range(1, len(result)):
        print(result[i])