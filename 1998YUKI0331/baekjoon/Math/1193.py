import sys
input = sys.stdin.readline


def solution(A):
    idx = 1
    sum = 0
    while True:
        sum += idx
        if sum >= A:
            break
        idx += 1

    if idx % 2 == 0:
        return str(idx + A - sum) + "/" + str(sum - A + 1)
    else:
        return str(sum - A + 1) + "/" + str(idx + A - sum)
  

if __name__ == '__main__':
    A = int(input())
    print(solution(A))
