# Read input
s = input()

count = 0

# Check each character
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

# Print result
print(count)
