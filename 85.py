from country_list import countries_for_language

listCountries = countries_for_language('en')

listCountries = [country[1] for country in listCountries]

with open('countries_raw.txt') as f:
    listCountriesRaw = f.read().splitlines()

listCountriesClean = [country for country in listCountriesRaw if country in listCountries]

with open('countries.txt', 'w') as f:
    for country in listCountriesClean:
        f.write(f"{country}\n")
