print(1, 2 , 6, 5)


def test_var_args(farg, *args):
    print ("formal arg:", farg)
    print(args)
    for arg in args:
        print ("another arg:", arg)

test_var_args(1, "two", 3)


def test_var_kwargs(farg, **kwargs):
    print ("formal arg:", farg)
    for key in kwargs:
        print ("another keyword arg: %s: %s" % (key, kwargs[key]))
    print (kwargs)


test_var_kwargs(farg=1, myarg2="two", myarg3=3)

#Zadanie1
# stworzyc słownik `{ 'first': funkcja1, 'second': funkcja2 }`, wczytać przez `input` klucz, wywołać funkcję
# zrób dwie funkcje i potem słownik i po wskazaniu klucza czy funkcja 1 czy 2 podaj wynik
def funkcja1(x):
    suma = 1 +1
    return suma

def funkcja2(x):
    roznica = 4 - 3
    return roznica

slownik = { 'first': funkcja1, 'second': funkcja2 }

klucz = input("Podaj klucz")

funkcja = slownik[klucz]
print(funkcja(2))