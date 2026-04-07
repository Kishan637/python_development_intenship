#palindrome check


def is_palindrome(text):
    return text == text[::-1]

word = input("Enter a word: ")

if is_palindrome(word):
    print("It is a palindrome")
else:
    print("Not a palindrome")