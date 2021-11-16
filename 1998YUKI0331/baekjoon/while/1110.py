N = input()
cycle = 0

if len(N) == 1:
    N = '0' + N

num = N
while True:
    cycle += 1
    temp = str(int(num[0]) + int(num[1]))
    if len(temp) == 1:
        temp = '0' + temp
    num = num[1] + temp[1]
    if num == N:
        break

print(cycle)
