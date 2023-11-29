import requests
from pprint import pprint

url = "https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)

pprint(response.json())
print()

# print(25*"*")
# print()
powierzchnia= response.json()[0]['area']
ludność= response.json()[0]['population']
print(f'Powierzchnia: {powierzchnia} km2')
print(response.json()[0]['area'])
print(response.json()[0]['population'])
print(response.json()[0]['currencies'])


#Zadanie 2

import requests
from pprint import pprint
import sys

if __name__ == '__main__':
    country = sys.argv[1]
    print(sys.argv)
    url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    response = requests.request(method="GET", url=url)

    content = response.json()
    content = content[0]
    capital = content['capital'][0]
    official1 = content['name']
    official = official1['official']
    print(official1)
    population = content['population']
    area = content['area']
    print(f'Nazwa  : \t {official}')
    print(f'Stolica: \t {capital}')
    print(f'Ludnosc: \t {population}')
    print(f'Pow.   : \t {area}')

