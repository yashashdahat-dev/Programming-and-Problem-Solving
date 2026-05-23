# Type your code here...
# Read input
s = input()

# Check palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
