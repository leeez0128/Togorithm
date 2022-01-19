"""
시간초과.
alphabets.remove(graph[nextX][nextY]) 해주는 이유?
현재 노드 기준 마지막에 방문한 노드가 최적 루트라는 보장이 없기 때문에
모든 경우를 순회하기 위해 지워준다.
안지워주면 A->B->C인 경우랑 C->A->B인 경우 같이 순서 다르게 가는 경우는 순회 안함
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dX = [-1, 1, 0, 0]
dY = [0, 0, -1, 1]


def solution(x, y, cnt):   # DFS
    global result
    alphabets.add(graph[x][y])
    result = max(result, cnt)

    for i in range(4):
        nextX = x + dX[i]
        nextY = y + dY[i]
        if 0 <= nextX < R and 0 <= nextY < C:
            if graph[nextX][nextY] not in alphabets:
                solution(nextX, nextY, cnt + 1)
                alphabets.remove(graph[nextX][nextY])


if __name__ == '__main__':
    R, C = map(int, input().strip().split())
    graph = [list(map(str, input().strip())) for _ in range(R)]
    alphabets = set()
    result = 1

    solution(0, 0, result)
    print(result)
