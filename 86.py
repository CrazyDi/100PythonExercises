from country_list import countries_for_language

listCountries = countries_for_language('en')

listCountries = [country[1] for country in listCountries]

checklist = ["Portugal", "Germany", "Munster", "Spain"]

print([country for country in checklist if country in listCountries])
