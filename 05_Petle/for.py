for i in range(12):
    print(i)

for i in range(3, 12): # 3- od kiedy zaczynami
    print(i)

for i in range(3, 12, 2): # 2- co ile wykonujemy krok
    print(i)

for c in "Ala ma kota":
    print(c)

for i in range(10):
    print(i)
else:
    print("Koniec")

for i in range(10):
    print(i)
    if i > 6:
        break
else:
    print("Koniec")

#Zadanie

n = int(input("Podaj liczbę:"))
print(f'Podałeś liczbę {n}')

suma = 0
while n > 0:
    suma += n % 10
    n //= 10

print(suma)

#inne rozwiązanie
liczba = input("Podaj liczbe")

suma_liczb = 0
for g in liczba:

    suma_liczb += int(g)

print(f"suma liczby{liczba} wynosi:{suma_liczb}")



- wczytaj przy użyciu `input()` liczbę; wypisz sumę jej cyfr

n=int(input('podaj liczbe'))
suma= n%10 + n//10
print(f'suma liczy {n} wynosi {suma}')

