__author__ = "Jeffrey Voke"
__title__ = "VOWEL COUNT"

def vowel_count(sentence):
    """
    Returns the count of vowels
    in a word or sentence.
    params: 
        sentence: str
    returns:
        count: int(count)
    """
    vowels = set('aeiouAEIOU')
    count = 0 
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count


if __name__ == '__main__':
    sentence = input("enter a word: ")
    print(f'The number of vowels: {vowel_count(sentence)}')