N, X = (input()).split()

A = list(map(int, input().split()))
for i in A:
    if i < int(X):
        print(i, end=' ')
