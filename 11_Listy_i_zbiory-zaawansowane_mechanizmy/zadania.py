#zadanie 1
# Stworzyć *list comprehension* na podstawie jednej listy z liczbami całkowitymi, ale z elementami o 6 większymi

range(10)
list(range(10))
[x+6 for x in range(10)]

# Zadanie 2
# - Stworzyć *list comprehension* tupli składających się z w/w liczb całkowitych i ich reprezentacji jako napis
#   - np. `[(1, "1"), (2, "2")]`

t = [(x, str(x)) for x in range(15)]
print(t)

#Zadanie 3
#  biorąc słownik `{"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}` stworzyć list comprehension nazw pojazdów cięższych niż 5000
#   - Nazwy podać dużymi literami (*uppercase*)

dane = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
[x.upper()for x in dane.keys() if dane[x]>5000]