def check_palindrome(numbers):
    results = {}
    for number in numbers:
        # Using the palindrome logic directly here
        if number == number[::-1]:
            results[number] = "Palindrome"
        else:
            results[number] = "Not Palindrome"
    return results

numbers = [
    "7489617719749244646336564429479177169847",
    "5485839837501070045005400701057389385845",
    "8025833559061079503003059701609553385208",
    "6593036601359343374664733439531066303956"
]

# Now, let's check which one is not a palindrome.
check_palindrome(numbers)