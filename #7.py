import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Iterate over the list in reverse order to safely modify it
i = len(random_numbers) - 1
while i >= 0:
    if random_numbers[i] % 2 == 1:
        # Remove odd numbers
        random_numbers.pop(i)
    else:
        # Replace even numbers with their double value
        random_numbers[i] *= 2
    i -= 1

print(random_numbers)
