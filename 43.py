import string

with open('letters2.txt', 'a') as f:
    for i in range(0, len(string.ascii_lowercase), 2):
        f.write(string.ascii_lowercase[i:(i+2)] + '\n')
