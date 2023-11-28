# Zadanie 2 moje rozwizanie
# - Dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną
#   - np. dla `73` wypisać `siedemdziesiąt trzy`


nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_dziesitek = {1: "dziesić",2: "dwadzieścia",3: "trzydzieści",4: "czterdzieści",5: "pięćdziesiąt",6: "seśćdziesiąt", siedemdziesiąt, osiemdziesiąt, dziewiećdziesiąt}
nazwy_jednosci.get(7, 'tej liczby nie znam')
a = []
while True:
    cyfra = input("Podaj liczbę od 1 do 999")
    if cyfra == "":
        break
    a.append(cyfra)
a.sort(key=int)
a
