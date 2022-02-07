import sys
from collections import deque
input = sys.stdin.readline

# p : RDD
# n : 4
# arr : [1, 2, 3, 4]
def solution(p, n, arr):
    for i in range(len(p)):
        if p[i] == 'R':
            arr.reverse()
        else: # 'D'
            if not arr:
                print("error")
                return
            else:
                arr.popleft()
                
    print("[", end="")
    for i in range(len(arr)):
        if i == len(arr) - 1:
            print(arr[i], sep="", end="")
        else:
            print(arr[i], ",", sep="", end="")
    print("]")

    

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        p = input().strip()
        n = int(input().strip())
        # arr = deque()
        arr = deque(input().strip().split("[")[1].split("]")[0])
        print("####", len(arr))
        # if len(temp) > 1:
        #     temp = temp.split(",")
        # for num in temp:
        #     arr.append(int(num))
        # solution(p, n, arr)