"""
create a program that
takes a user's name and 
age and prints a greeting
message.
"""
def greeting(name:str, age:int):
    print(f'Hello, {name} you mentioned that your age is {age}. \
It is nice to have you for the immersion class.')

if __name__ == '__main__':
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(greeting(name,age))

