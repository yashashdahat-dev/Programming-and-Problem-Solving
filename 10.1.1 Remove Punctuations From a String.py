# Type Content here...
# Read input
s = input()

result = ""

# Keep only letters, digits, and spaces
for ch in s:
    if ch.isalnum() or ch == " ":
        result += ch

# Print result
print(result)
