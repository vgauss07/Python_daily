"""
create a program that swaps the 
values of two variables
"""

def varSwap(a,b):
    b = a - b
    a = a - b
    return b,a

if __name__ == "__main__":
    a = int(input("Enter variable value: "))
    b = int(input("Enter variable value: "))
    print(varSwap(a,b))

