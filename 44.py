import string

with open('letters3.txt', 'a') as f:
    for i in range(0, len(string.ascii_lowercase), 3):
        f.write(string.ascii_lowercase[i:(i+3)] + '\n')
