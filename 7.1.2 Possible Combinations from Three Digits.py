a, b, c = input().split()


digits = [a, b, c]


print(digits[0] + digits[1] + digits[2])
print(digits[0] + digits[2] + digits[1])
print(digits[1] + digits[0] + digits[2])
print(digits[1] + digits[2] + digits[0])
print(digits[2] + digits[0] + digits[1])
print(digits[2] + digits[1] + digits[0])
