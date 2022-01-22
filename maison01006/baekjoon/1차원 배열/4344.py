import sys
input = sys.stdin.readline


def solution(arr):
    for students in arr:
        sum = 0

        for socre in students[1:]:
            sum += socre
        answer = [x for x in students[1:] if x > sum/students[0]]
        print("{:.3f}%".format(len(answer)/students[0]*100))


if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(arr)
