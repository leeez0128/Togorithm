import sys
input = sys.stdin.readline


def solution(word):
    cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    result = 0
    for atia in cro:
        result += word.count(atia)
    
    print(len(word)-result)
            



if __name__ == '__main__':
    word = input().strip()
    solution(word)