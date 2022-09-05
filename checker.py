from password import pwd

def check(temp):
    if type(temp) != str:
        return False
    else:
        if len(temp) != len(pwd):
            return False
        else:
            for char_a, char_b in zip(temp, pwd):
                if char_a != char_b:
                    return False
    return True