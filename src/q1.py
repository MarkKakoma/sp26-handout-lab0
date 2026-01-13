"""
Please implement the stub function to match the documentation.
Make sure to implement tests in the tests directory.
"""


def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.

    Args:
        s (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s_lower = s.lower()
    return s_lower == s_lower[::-1]

# Test cases
assert is_palindrome("racecar") == True
assert is_palindrome("a") == True
assert is_palindrome("change") == False
    
