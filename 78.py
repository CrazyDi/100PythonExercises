from random import sample

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

result = ''

for i in sample(range(0, len(characters)), 6):
    result += characters[i]

print(result)
