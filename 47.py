import glob

letters = []
file_list = glob.glob("letters/*")

for filename in file_list:
    with open(filename) as f:
        l = f.read().strip("\n")
        if l in "python":
            letters.append(l)

print(letters)