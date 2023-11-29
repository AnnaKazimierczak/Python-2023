l = list(range(5, 10))
print(l)
try:
    i = int(input("podaj indeks "))
    print(f'Pod indeksem {i} jest element {l[i]}')
except IndexError as e:
    print(e)
else:
    print("Koniec")
finally:
    print("Finally")

#Zadanie- moje rozwiązanie- błąd

n=0
while True:
    try:
        n=int(input('podaj liczbe'))
    except ValueError as e:
        print('Zły format danych.Wpisz ponownie.')
        print(e)
    else:
        braek

n = int(input('podaj liczbe'))
suma = n % 10 + n // 10
print(f'suma liczy {n} wynosi {suma}')

#Zadanie- inne rozwiązanie do analizy

liczba = 0
while True:
    try:
        liczba = input("Podaj liczbę naturalną: ")
        liczba = int(liczba)
    except ValueError as e:
        print (f"{liczba} nie jest liczbą!")
    else:
        break

suma = 0
i = liczba
while i > 0:
    suma += i%10
    i //= 10
    print (f'Suma cyfr podanej liczby {liczba} wynosi {suma}')