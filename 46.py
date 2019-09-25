import glob

letters = []
file_list = glob.glob("letters/*")

for filename in file_list:
    with open(filename) as f:
        letters.append(f.read().strip("\n"))

print(letters)