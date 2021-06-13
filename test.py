
import sys

from acclibrary import Saldo, Zakup, Sprzedaz

# current = open("out.txt", "a")
with open("in.txt") as data:

    konto = {}
    magazyn = []

    while True:
        akcja = data.readline().rstrip()
        if not akcja:
            break

        elif akcja == "saldo":
            operacja = data.readline().rstrip()
            comment = data.readline().rstrip()
            konto[akcja] = Saldo(operacja, comment)
            for dane, jaja in konto.items():
                jaja.write()