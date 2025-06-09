

"""
At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.

"""

def nb_year(p0, percent, aug, p):
    count = 0  # to count each period
    percent = percent/100
    while p0 < p:
        p0 += (p0*percent) + aug
        count += 1
    return count


if __name__ == '__main__':
    p0 = int(input("Enter initial pop. no: "))
    percent = float(input("Enter percent values: "))
    aug = int(input("Enter value: "))
    p = int(input("Enter expected pop. value: "))
    print(f'It will need {nb_year(p0,percent,aug,p)} years')