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
    
    return True