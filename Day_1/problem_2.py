"""
Create a Celsius to Fahrenheit
converter.
"""
def tempConverter(c_value):
    return (9/5) * c_value + 32


if __name__ == '__main__':
    c_value = float(input("Enter Celsius Value: "))
    print(f'The temperature in Fahrenheit is: {tempConverter(c_value)}')

