import sys
input = sys.stdin.readline


def solution(S):
    S = S.upper()
    cnt = {}
    for i in S:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 0

    sort = sorted(cnt.values(), reverse=True)
    if len(sort) >= 2 and sort[0] == sort[1]:
        return "?"
    else:
        return [key for key, value in cnt.items() if value == sort[0]][0]
        # [key for key, value in cnt.items() if value == sort[0]]는 ['A'] 이런 모양


if __name__ == '__main__':
    S = input().strip()
    print(solution(S))
