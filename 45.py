import string, os

os.mkdir('letters')
for l in string.ascii_lowercase:
    with open('letters/' + l, 'w') as f:
        f.write(l)
