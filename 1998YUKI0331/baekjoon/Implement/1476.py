import sys
input = sys.stdin.readline


def solution(E, S, M):
    E_i, S_i, M_i, result = 1, 1, 1, 1

    while True:
        if E_i == E and S_i == S and M_i == M:
            return result

        E_i += 1
        S_i += 1
        M_i += 1
        result += 1

        if E_i == 16:
            E_i -= 15
        if S_i == 29:
            S_i -= 28
        if M_i == 20:
            M_i -= 19


if __name__ == '__main__':
    E, S, M = map(int, input().strip().split())
    print(solution(E, S, M))
