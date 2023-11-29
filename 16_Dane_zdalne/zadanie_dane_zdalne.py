import requests
from pprint import pprint

url = "https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)

pprint(response.json())
print()

# print(25*"*")
# print()
print(response.json()[0]['area'])
print(response.json()[0]['population'])
print(response.json()[0]['currencies'])