#Zadanie
# - Stwórz czytnik plików CSV bez użycia modułu CSV
#   - napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
#   - wypisze jego zawartość oddzielając pola tabulacją `\t`

import csv
import os
import sys
print(os.getcwd())
tab = '\t'
n = 0
with open(sys.argv[1]) as csvfile:
    for line in csvfile:
        print(f'{n:03d} {tab.join(line.strip().split(","))}')
        n +=1

