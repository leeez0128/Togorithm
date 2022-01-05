import sys
input = sys.stdin.readline


def solution(N, road, oil):
    result = 0
    min_oil = oil[0]
    result += min_oil * road[0]

    for i in range(1, N - 1):
        min_oil = min(min_oil, oil[i])
        result += min_oil * road[i]

    return result


if __name__ == '__main__':
    N = int(input())
    road = list(map(int, input().split()))
    oil = list(map(int, input().split()))
    print(solution(N, road, oil))
