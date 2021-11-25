# https://readytoearndon.tistory.com/11

import sys
input = sys.stdin.readline


def solution(star):
    result = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:
            result.append(star[i % len(star)] + " " * len(star) + star[i % len(star)])
        else:
            result.append(star[i % len(star)] * 3)
    return result


star = ["***", "* *", "***"]
N = int(input())
# for i in range(int(N ** (1 / 3)) - 1):
#     star = solution(star)

e = 0
while N != 3:
    N = int(N / 3)
    e += 1

for i in range(e):
    star = solution(star)
for i in star:
    print(i)
