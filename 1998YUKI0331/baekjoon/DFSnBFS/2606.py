import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, result):
    check[start] = True
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        result.append(v)

        for w in range(len(graph[v])):
            if graph[v][w] == 1 and check[w] is False:
                check[w] = True
                queue.append(w)


if __name__ == '__main__':
    N = int(input())
    V = int(input())
    A = [list(map(int, input().split())) for _ in range(V)]
    result = []

    graph = [[0] * (N + 1) for _ in range(N + 1)]
    check = [False] * (N + 1)
    for i in range(len(A)):
        graph[A[i][0]][A[i][1]] = graph[A[i][1]][A[i][0]] = 1

    bfs(1, result)
    print(len(result) - 1)
