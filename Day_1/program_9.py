"""
Write a program to 
convert days into years, weeks
and days.
"""
def days_converter(days):
    if days < 7:
        return days
    elif 7 <= days <= 30:
        weeks = days // 7
        day = days - weeks
        return weeks, day
    elif days
