def is_valid_url(url):
    """
    Checks if the passed string is a valid URL.

    Param: - url: The string to check.

    Return: - True if the string is a basic valid URL, False otherwise.
    """
    # Check if '://' is in the URL
    if '://' not in url:
        return False

    # Split the URL by '://' to separate the host
    scheme, host = url.split('://', 1)

    # Check the scheme
    if scheme not in ['http', 'https']:
        return False

    # Check if there's at least one dot in the host
    if '.' not in host:
        return False

    return True

# Examples
print(is_valid_url("https://www.python.com"))  # Expected to return True
print(is_valid_url("ftp://youtube.com"))  # Expected to return False(we only accept http and https)
print(is_valid_url("http//x"))  # Expected to return False (missing ':')
print(is_valid_url("https://chatgpt"))  # Expected to return False (missing dot)
