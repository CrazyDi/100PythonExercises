password = input('Enter password: ')

isDigit = False
isUpper = False

for i in range(0, len(password)):
    if password[i].isdigit():
        isDigit = True

    if password[i].upper() == password[i]:
        isUpper = True

if len(password) >= 5 and isDigit and isUpper:
    print('Password is fine!')
else:
    print('Password is not fine!')
