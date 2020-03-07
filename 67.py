def translate(word):
    try:
        d = dict(weather="clima",
                 earth="terra",
                 rain="chuva")
        return d[word]
    except KeyError:
        return "That word doesn't exist!"


word = input("Enter a word: ")
print(translate(word))
