import sys
from collections import deque
input = sys.stdin.readline


def solution(N, K, graph):
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        dX = [x + 1, x - 1, x * 2]
        if x == K:
            return graph[x]

        for i in range(3):
            nextX = dX[i]
            if 0 <= nextX <= 100000 and graph[nextX] == 0:
                graph[nextX] = graph[x] + 1
                queue.append((nextX))


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    graph = [0 for _ in range((100001))]  # 범위 넘어가서 가는게 빠를 수도 있어...

    print(solution(N, K, graph))
