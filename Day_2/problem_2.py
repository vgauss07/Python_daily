"""
Ask the user for a number. 
Depending on whether the number is even or odd, 
print out an appropriate message to the user.
"""

def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == '__main__':
    number = int(input("Enter number: "))
    print(f'The number {number}, is {even_odd(number)}')