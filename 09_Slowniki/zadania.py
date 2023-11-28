# Zadanie 2
# - Dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną
#   - np. dla `73` wypisać `siedemdziesiąt trzy`

a = []
while True:
    cyfra = input("Podaj liczbę od 1 do 999")
    if cyfra == "":
        break
    a.append(cyfra)
    print(a)