import sys
input = sys.stdin.readline


def get_stars(n):
    result = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            result.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            result.append(n[i % len(n)] * 3)
    return result


star = ["***", "* *", "***"]
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e += 1

for i in range(e):
    star = get_stars(star)
for i in star:
    print(i)
