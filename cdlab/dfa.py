import re
def check_regularexp(exp):
    regular= re.compile('a*|a*b+|abb')
    if(re.fullmatch(regular,exp)):
        return True
    return False
print(check_regularexp('abb'))