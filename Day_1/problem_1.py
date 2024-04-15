# calulcate sums of numbers
# entered by a user

def sum_numbers(number_1, number_2):
    return number_1 + number_2


if __name__ == "__main__":
    number_1 = int(input('Enter number: '))
    number_2 = int(input('Enter number: '))
    print(f'The sum is: {sum_numbers(number_1, number_2)}')