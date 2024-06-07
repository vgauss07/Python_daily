"""
Create a program that asks the user to enter 
their name and their age. Print out a message 
addressed to them that tells them 
the year that they will turn 100 years old
"""
def year_100(name, age):
    from datetime import datetime
    today = datetime.today()
    birth_year = today.year - age
    if age < 100:
        year_of_100 = birth_year + 100
    return year_of_100


if __name__ == '__main__':
    name = input("Enter your name: ")
    age = int(input("Enter your age:  "))
    print(f'The year {name} will be 100 years in the year: {year_100(name, age)}')
