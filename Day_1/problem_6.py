"""
create a program that finds 
the minimum and maximum values
from a list
"""

# lets create a list input 
# for users

lst = []

def maxMin(lst:list): 
    max_value = max(lst)    
    min_value = min(lst)
    
    print(f'maximum value: {max_value}')
    print(f'minimum value: {min_value}')

if __name__ == '__main__':
    n = int(input("Enter the number of elements"))
    for i in range(1, n+1):
        ele = int(input())
        lst.append(ele)
    maxMin(lst)
