def find_pattern_occurrences(text):
        # Divide the text into words
    words = text.split()

    # Initialize a count of matches
    count = 0

    # Use for to go through the loop and find occurrences
    for word in words:
        # Check if the word starts with "un" and ends with "an"
        if word.startswith("un") and word.endswith("an"):
            count += 1  # Increment the count for each match

    # Return the total count of occurences
    return count

# Example
text = "The unusual plan was to understand the mechanism of the unban command."
print(find_pattern_occurrences(text))
