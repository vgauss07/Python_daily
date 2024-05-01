"""
Given a list of integers, 
find the sum of all positive
integers
"""

# step 1: let the user put the values in the list
# filter out the positive integers
# sum and return sum

lst = []

def pos_sum(lst:list):
    sum = 0
    for i in lst:
        if i > 0:
            sum += lst[i]
    return sum


if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    for x in range(1, n):
        ele = int(input())
    print(pos_sum(lst))

