def count_words(fname):
    with open(fname) as f:
        str = f.read().split()
        res = []
        for s in str:
            r = s.split(',')
            res = res + r
        return len(res)


print(count_words('words2.txt'))
