import sys
input = sys.stdin.readline


def solution(arr):
    for results in arr:
        score = 1
        answer = 0
        for result in list(str(results)):
            if result == 'O':
                answer += score
                score += 1
            else:
                score = 1
        print(answer)


if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(input().strip().split()))
    solution(arr)
