import sys
from collections import deque
input = sys.stdin.readline


def dfs(start):
    check1[start - 1] = True
    print(start, end=' ')

    for w in range(len(graph[start])):
        if graph[start][w] == 1 and check1[w - 1] is False:
            dfs(w)


def bfs(start):
    check2[start - 1] = True
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for w in range(len(graph[v])):
            if graph[v][w] == 1 and check2[w - 1] is False:
                check2[w - 1] = True
                queue.append(w)


if __name__ == '__main__':
    N, M, V = map(int, input().strip().split())
    A = [list(map(int, input().split())) for _ in range(M)]

    graph = [[0] * (N + 1) for _ in range(N + 1)]
    check1 = [False] * N
    check2 = [False] * N
    for i in range(len(A)):
        graph[A[i][0]][A[i][1]] = graph[A[i][1]][A[i][0]] = 1

    dfs(V)
    print()
    bfs(V)
