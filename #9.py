def days_since_birthday(birthday):
    # Split the string into day, month, and year
    day, month, year = birthday.split('-')

    # Convert everything to integers
    day = int(day)
    month = int(month)
    year = int(year)

    # Get the current year
    current_year = 2024

    # Calculate the number of years passed and subtract 1 to exclude the birth year
    years_passed = current_year - year - 1

    # Calculate the number of days
    days_passed = years_passed * 365

    return days_passed

# my birthday example
birthday = "09-06-2023"
print(days_since_birthday(birthday))
