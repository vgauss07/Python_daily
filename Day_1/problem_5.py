"""
Write a program to 
determine if a number is
even or odd
"""

def even_or_odd(number:int):
    if number % 2 == 0:
        print("Even Number")
    elif number % 2 != 0:
        print("Odd Number")

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    even_or_odd(number)