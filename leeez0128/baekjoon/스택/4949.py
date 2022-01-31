import sys
input = sys.stdin.readline


def solution(sen):
    stack = []
    result = 1
        
    for ch in sen:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = 0
                break
    
    if result == 1:
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    while True:
        sen = input().strip()
        if sen == '.':
            break
        solution(sen)
