# Create a Python module with functions to check palindrome,
# count vowels, and find frequency of letters.

def ispalindrome(name):
    if name == name[::-1]:
        return "Yes, it is a palindrome."
    else:
        return "No, it is not a palindrome."


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in name:
        if ch in vowels:
            count += 1

    return count


def frequency_of_letters(name):
    frequency = {}

    for ch in name:
        if ch != " ":
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

    return frequency