
import sys

from acclibrary import Zakup, Sprzedaz, save_saldo, save_zakup, save_sprzedaz

with open("in.txt") as data:

    konto = {"saldo": 0}
    magazyn = {}

    while True:
        akcja = data.readline().rstrip()
        if not akcja:
            break

        elif akcja == "saldo":
            operacja = int(data.readline().rstrip())
            comment = data.readline().rstrip()
            if konto["saldo"] + operacja < 0:
                print("Niewystarczające środki na koncie.")
                break
            konto["saldo"] += operacja
            save_saldo(akcja, operacja, comment)

        elif akcja == "zakup":
            produkt = data.readline().rstrip()
            cena = int(data.readline().rstrip())
            ilosc = int(data.readline().rstrip())
            magazyn[akcja] = Zakup(produkt, cena, ilosc)
            save_zakup(akcja, produkt, cena, ilosc)

        elif akcja == "sprzedaz":
            produkt = data.readline().rstrip()
            cena = data.readline().rstrip()
            ilosc = data.readline().rstrip()
            magazyn[akcja] = Sprzedaz(produkt, cena, ilosc)
            save_sprzedaz(akcja, produkt, cena, ilosc)

        elif akcja == "stop":
            break

print(konto)
# wrapper(sys.argv[1], konto, magazyn)
