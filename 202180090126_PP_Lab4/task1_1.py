import re

pattern=r'^(?:\w+[- .,_]){4}\w+$'
def check_password(password):
    return bool(re.match(pattern, password))

print(check_password(input(f'regular exfression: {pattern}\nEnter your password: ')))

