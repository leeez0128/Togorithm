"""
처음에 플로이드 와샬로 풀었는데 메모리 초과 났음.
왜냐 ? 플로이드는 N->N의 최단 경로를 찾는 알고리즘으로 시간 복잡도가 O(V^3) 임.
이 문제는 1->N의 최단 경로를 찾는 문제기 때문에 플로이드까지 안가도 됨.
다익스트라(1->N) 선에서 끝내야 된다.
"""

import sys
import heapq   # PriorityQueue
input = sys.stdin.readline


def solution(V, E, K, graph, dist):  # 다익스트라
    dist[K] = 0
    heap = []
    heapq.heappush(heap, (0, K))

    while heap:
        wei, now = heapq.heappop(heap)
        if dist[now] < wei:   # 더 짧은 경로 알고 있으면 무시
            continue

        for i in graph[now]:  # 인접 노드 검사
            next_wei = wei + i[1]
            if dist[i[0]] > next_wei:
                dist[i[0]] = next_wei
                heapq.heappush(heap, (next_wei, i[0]))

    dist = list(map(lambda x: "INF" if x == float("inf") else x, dist[1:]))

    return dist


if __name__ == '__main__':
    V, E = map(int, input().strip().split())
    K = int(input())
    graph = [[] for _ in range(V + 1)]
    dist = [float("inf") for _ in range(V + 1)]

    for _ in range(E):
        u, v, e = map(int, input().strip().split())
        graph[u].append((v, e))

    print(*solution(V, E, K, graph, dist), sep="\n")
