H, M = (input()).split()

result = (int(H) * 60 + int(M)) - 45

if result >= 0:
    print(int(result / 60), result % 60)
else:
    print("23", 60 + result)
