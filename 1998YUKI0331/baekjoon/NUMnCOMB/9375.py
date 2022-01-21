import sys
input = sys.stdin.readline


def solution(N, A):
    answer = 1
    dict = {}

    for i in A:
        if i[1] in dict:
            dict[i[1]].append(i[0])
        else:
            dict[i[1]] = [i[0]]

    for val in dict.values():
        answer *= (len(val) + 1)

    return answer - 1


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = [list(map(str, input().split())) for _ in range(N)]
        print(solution(N, A))
