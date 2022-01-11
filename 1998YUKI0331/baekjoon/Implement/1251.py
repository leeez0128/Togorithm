import sys
input = sys.stdin.readline


def solution(S):
    words = []
    for i in range(1, len(S) - 1):
        for j in range(i + 1, len(S)):
            temp = S[0:i][::-1] + S[i:j][::-1] + S[j:len(S)][::-1]
            words.append(temp)

    return sorted(words)[0]


if __name__ == '__main__':
    S = input().strip()
    print(solution(S))
