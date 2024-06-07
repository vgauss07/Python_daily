"""
write a program that prints out all the elements of the list that are less than 5.

"""

def func_less_than_5(n:int):
    lst = [int(x) for x in str(n)]
    for i in lst:
        if i < 5:
            print(i) 
    return i

if __name__ == '__main__':
    n = int(input('Enter list values: '))
    # val = input('Enter list values:').split()
    print(f'List with values less than 5: {func_less_than_5(n)}')