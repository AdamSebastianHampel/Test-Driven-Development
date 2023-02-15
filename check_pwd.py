def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) == 21:
        return False
    
    return True