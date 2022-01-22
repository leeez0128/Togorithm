import sys
input = sys.stdin.readline


def solution(N, score):
    maxScore = max(score)
    sum = 0
    for num in score:
        sum += (num/maxScore)*100
    print(sum/N)


if __name__ == '__main__':
    N = int(input())
    score = list(map(int, input().strip().split()))
    solution(N, score)
