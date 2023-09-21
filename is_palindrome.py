punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def is_palindrome(teststr):
    clean_str = "".join(char for char in teststr if char not in punct).replace(" ", "")
    reversed_str = clean_str[::-1]
    return True if clean_str.lower() == reversed_str.lower() else False


def is_palindrome_2(teststr):
    clean_str = ""
    for char in teststr:
        if char.isalnum():
            # is alphanumeric is a built-in python function that removes every character that are not alphanumeric (spaces, punctuation etc.)
            clean_str += char

    reversed_str = ""
    i = len(clean_str) - 1

    while i >= 0:
        reversed_str += clean_str[i]
        i -= 1

    if clean_str.lower() == reversed_str.lower():
        return True
    else:
        return False
