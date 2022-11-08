correctPassword = False

while not correctPassword:
    password = input('Enter password: ')

    isDigit = False
    isUpper = False

    result = ''

    for i in range(0, len(password)):
        if password[i].isdigit():
            isDigit = True
        else:
            if password[i].upper() == password[i]:
                isUpper = True

    if not isDigit:
        result += 'You need at least one number. /n'

    if not isUpper:
        result += 'You need at least one uppercase letter /n'

    if len(password) < 5:
        result += 'You need at least 5 characters'

    if result == '':
        result = 'Password is fine!'
        correctPassword = True

    print(result)