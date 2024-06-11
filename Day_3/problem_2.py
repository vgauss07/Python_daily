__author__ = "Jeffrey Voke"
__title__ = "exes and ohs"

def xo(s:str):
    """
    checks a string for counts
    of 'x' and 'o' and returns 
    a boolean value.
    Params:
        s: str
        o: int
        x: int
    Returns:
        True or False: bool.
    """
    o = s.lower().count('o')
    x = s.lower().count('x')

    if o == x:
        return True
    elif o !=x:
        return False
    else:
        return True


if __name__ == '__main__':
    s = input('Enter word:')
    print(f'Answer: {xo(s)}')