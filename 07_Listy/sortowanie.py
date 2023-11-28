lista = list(range(10, 0, -1))
lista
lista.sort()
lista
lista.sort(reverse=True)
lista
lista = [ str(i) for i in range(21)]
lista
lista.sort()
str(lista)
lista.sort(key=int)
str(lista)

dluga_lista = [ str(i) for i in range(21)] + [ str(i) for i in range(-1, -21, -1)]
str(dluga_lista)
dluga_lista.sort(key=int)


#Zadanie 2
l = []
while True:
    liczba = input("Podaj liczbę, a dodam ją do listy: ").strip()
    if liczba == "":
        break
    l.append(int(liczba))
l.sort()
for i in range(1, len(l)):
    if l[-1*i]%2 == 0:
        print(f"Ostatnia parzysta liczba to: {l[-1*i]}")
        break
