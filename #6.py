# First
list1 = [1, 2, 3, 4, 5]
print("Original list:", list1)


# Change one element
list1[0] = 10


# List after modification
print("List after changes:", list1)

# Unmutable
string1 = "Hello"
print("Original string:", string1)

# Trying to change
try:
    string1[0] = "J"
except TypeError as e:
    print("Error:", e)

# String after attempted modification
print("String after modification attempt:", string1)
