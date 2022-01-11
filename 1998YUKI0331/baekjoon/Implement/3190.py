import sys
from collections import deque
input = sys.stdin.readline


def printMap(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print(graph[i][j], end=" ")
        print()
    print()


def change(dir, c):   # 상(0) 우(1) 하(2) 좌(3)
    if c == "L":
        dir = (dir - 1) % 4
    elif c == "D":
        dir = (dir + 1) % 4
    return dir


dX = [-1, 0, 1, 0]   # 상 우 하 좌
dY = [0, 1, 0, -1]


def solution(x, y, N, graph, direction):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2  # 뱀 위치는 2로 표시
    cur_dir = 1
    count = 1

    while queue:
        x = x + dX[cur_dir]
        y = y + dY[cur_dir]
        # printMap(graph)
        if 0 <= x < N and 0 <= y < N and graph[x][y] != 2:
            if graph[x][y] == 1:             # 사과 있는 경우
                graph[x][y] = 2
                queue.append((x, y))
            else:                            # 사과 없는 경우
                tail_x, tail_y = queue.popleft()
                graph[tail_x][tail_y] = 0
                graph[x][y] = 2
                queue.append((x, y))
                
            if count == int(direction[0][0]):    # 방향 변경
                cur_dir = change(cur_dir, direction[0][1])
                if len(direction) > 1: direction.pop(0)

            count += 1

        else:
            return count
    


if __name__ == '__main__':
    N = int(input())
    graph = [[0] * (N) for _ in range(N)]
    K = int(input())
    for _ in range(K):
        i, j = map(int, input().strip().split())
        graph[i - 1][j - 1] = 1
    L = int(input())
    direction = [list(map(str, input().split())) for _ in range(K)]

    print(solution(0, 0, N, graph, direction))
