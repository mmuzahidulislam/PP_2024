import re

pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*?]).{8,}$'
def check_password(password):
    if re.fullmatch(pattern,password): print('your password is correct!')
    else: print('Wrong password!')

check_password(input(f'regular expression : {pattern}\nEnter your password: '))