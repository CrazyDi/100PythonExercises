with open('countries_missing.txt') as f:
    listCountries = f.read().splitlines()

checklist = ["Portugal", "Germany", "Spain"]

for country in checklist:
    listCountries.append(country)

with open('countries_full.txt', 'w') as f:
    f.write('\n'.join(listCountries))
