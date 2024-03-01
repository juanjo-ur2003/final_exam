#1



#3
import datetime
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print (a)
print(b)
c = a + b
print(c)
d = "abc" * (c//3)
print(d)

#4
def check_palindrome(numbers):
    results = {}
    for number in numbers:
        # Using the palindrome logic
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