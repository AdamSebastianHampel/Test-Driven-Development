def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    
    if pwd == '123456789':
        return False
    
    return True