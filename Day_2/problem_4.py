__author__ = 'JeffreyVoke'
"""
Create a program that asks the user for a number and then prints out 
a list of all the divisors of that number. (If you don’t 
know what a divisor is, it is a 
number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 
has no remainder.)
"""



def all_divisors(num:int):
    divisorList = []
    for i in list(range(1, num+1)):
        if num % i == 0:
            divisorList.append(i)
    return divisorList


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print(f'The divisors are: {all_divisors(num)}')

