__author__ = "Jeffrey Voke"
__title__ = "Unique in Order"

"""
Implement the function unique_in_order
 which takes as argument a sequence and 
 returns a list of items without any elements 
 with the same value next to each other 
and preserving the original order of elements.

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

"""
def unique_in_order(sequence:list):
    """
    param:
        sequence:str
    returns
        order unique values:list
    """
    # convert to list 
    val = list(sequence)
    # initialize values
    n = 0
    m = 1

    for i in val[:-1]:
        if val[n] == val[m]:
            val.pop(m)
        else:
            n += 1
            m += 1
    return val


    if __name__ == '__main__':
        sequence = input("Enter values: ")
        print(unique_in_order(sequence))


