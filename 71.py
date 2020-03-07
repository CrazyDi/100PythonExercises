import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt", headers={'user-agent': 'customUserAgent'})
print(r.text.count("a"))
