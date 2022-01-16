import sys
input = sys.stdin.readline

"""
def solution(x, N, graph, dist):  #DFS
    for i in range(N):
        if graph[x][i] == 1 and dist[i] == 0:
            dist[i] = 1
            solution(i, N, graph, dist)


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        dist = [0 for _ in range(N)]
        solution(i, N, graph, dist)
        print(*dist, sep=" ")
"""


def solution(N, graph):  # 플로이드 와샬 (PyPy3)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                    graph[i][j] = 1

    return graph


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        print(*solution(N, graph)[i], sep=" ")
