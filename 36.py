def count_words(fname):
    with open(fname) as f:
        s = f.read().split()
        return len(s)


print(count_words('words2.txt'))
