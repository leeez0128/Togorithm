num1 = int(input())
num2 = input()

result1 = num1 * int(num2[2])
result2 = num1 * int(num2[1])
result3 = num1 * int(num2[0])

print(result1)
print(result2)
print(result3)
print(int(result1) + int(result2)*10 + int(result3)*100)
