"""
write a program to calculate compound
interest given all parameters
"""

def compound_interest(p:float,r:float, n:int, t:int):
    return p*(1 + (r/n))**(n*t)


if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter interest rate: "))
    n = int(input("Enter number of times the interest applies: "))
    t = int(input("Enter timeframe: "))
    print(compound_interest(p,r,n,t))



