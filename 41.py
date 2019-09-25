import string

with open('letters.txt', 'a') as f:
    for l in string.ascii_lowercase:
        f.writelines(l)
        f.write('\n')
