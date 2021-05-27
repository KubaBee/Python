import re

phoneNumberRegex2 = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
mo2 = phoneNumberRegex2.search('todays date is 28/02/2021')



print(f'DAY: {mo2.group(1)} MONTH: {mo2.group(2)} YEAR: {mo2.group(3)}')

day = int(mo2.group(1))
month = int(mo2.group(2))
year = int(mo2.group(3))

def is_vaild():
    if day > 31:
        return False
    if month == {4, 6, 9, 11}:
        if day != 30:
            return False
    if year % 400 == 0 or year % 4 == 0 and year % 100 == 0:
        if month == 2:
            if day != 29:
                return False
    else:
        if day != 28:
            return False
    return True


print("Is this date vaild? " + str(is_vaild()))