__author__ = "Jeffrey Voke"
__title__ = "Your Order, Please"

"""
Your task is to sort a given string. Each word in the string will
contain a single number.
 This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid
consecutive numbers.

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of
th5e pe6ople"
""  -->  ""
"""
# ________________step1_______________________

# extract the numbers from the words


def digit(words):
    import re
    numbers = re.findall(r'\d+', words)
    return int(' '.join(numbers)) if numbers else ('inf')
# step 2: create a function to sort the sentence
# based on the numbers in the string


def sort_sentence(sentence):
    word = sentence.split()  # to process each word individually
    sorted_words = sorted(word, key=digit)
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence


if __name__ == '__main__':
    sentence = input("Enter words: ")
    print(f'This is the sorted sentence: {sort_sentence(sentence)}')
