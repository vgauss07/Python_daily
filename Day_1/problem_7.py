"""
Check if a string is a palindrome
"""

word = "ABCDE"

def palindrome_check(word):
    if word[:] == word[-1:]:
        print("Palindrome")
    else:
        print("Not a palindrome")

if __name__== "__main__":
    palindrome_check(word)