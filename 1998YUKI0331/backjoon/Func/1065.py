import sys
input = sys.stdin.readline


def solution(N):
    if N < 100:
        return N
    else:
        result = 0
        for i in range(N + 1):
            if (i < 101):
                continue
            sum = int(str(i)[0]) + int(str(i)[2])
            if sum == 2 * int(str(i)[1]):
                result += 1
        return result + 99


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
