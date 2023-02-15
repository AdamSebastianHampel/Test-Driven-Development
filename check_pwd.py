import string

def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    lower = 0
    lowerStr = string.ascii_lowercase
    for i in pwd:
        if i in lowerStr:
            lower = 1
            break
    if lower == 0:
        return False

    upper = 0
    upperStr = string.ascii_uppercase
    for i in pwd:
        if i in upperStr:
            upper = 1
            break
    if upper == 0:
        return False


    digit = 0
    digitStr = string.digits
    for i in pwd:
        if i in digitStr:
            digit = 1
            break
    if digit == 0:
        return False

    symbol = 0
    symbolStr = "~`!@#$%^&*()_+-="
    for i in pwd:
        if i in symbolStr:
            symbol = 1
            break
    if symbol == 0:
        return False

    return True
