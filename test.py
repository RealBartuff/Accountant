
import sys

from acclibrary import Saldo, Zakup, Sprzedaz, save_saldo, save_zakup, save_sprzedaz, stop

with open("in.txt") as data:

    konto = {}
    magazyn = {}

    while True:
        akcja = data.readline().rstrip()
        if not akcja:
            break

        elif akcja == "saldo":
            operacja = data.readline().rstrip()
            comment = data.readline().rstrip()
            konto[akcja] = Saldo(operacja, comment)
            for sl, item in konto.items():
                item.write()
            save_saldo(akcja, operacja, comment)

        elif akcja == "zakup":
            produkt = data.readline().rstrip()
            cena = data.readline().rstrip()
            ilosc = data.readline().rstrip()
            magazyn[akcja] = Zakup(produkt, cena, ilosc)
            for k, v in magazyn.items():
                v.write()
            save_zakup(akcja, produkt, cena, ilosc)

        elif akcja == "sprzedaz":
            produkt = data.readline().rstrip()
            cena = data.readline().rstrip()
            ilosc = data.readline().rstrip()
            magazyn[akcja] = Sprzedaz(produkt, cena, ilosc)
            for k, v in magazyn.items():
                v.write()
            save_sprzedaz(akcja, produkt, cena, ilosc)

        elif akcja == "stop":
            stop(akcja)
            break
