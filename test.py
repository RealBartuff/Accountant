
import sys

from acclibrary import save_saldo, save_zakup, save_sprzedaz, stop

with open("in.txt") as data:

    konto = {"saldo": 0}
    magazyn = []

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
            produkt = str(data.readline().rstrip())
            cena = int(data.readline().rstrip())
            ilosc = int(data.readline().rstrip())
            if konto["saldo"] < cena * ilosc:
                print("Niewystarczające środki na koncie.")
                break
            else:
                konto["saldo"] -= cena * ilosc
            towar = {}
            towar[produkt] =+ ilosc
            magazyn.append(towar)
            save_zakup(akcja, produkt, cena, ilosc)

        elif akcja == "sprzedaz":
            produkt = str(data.readline().rstrip())
            cena = int(data.readline().rstrip())
            ilosc = int(data.readline().rstrip())
            if produkt not in towar:
                print("Brak towaru w magazynie.")
                break
            else:
                towar[produkt] -= ilosc
            konto["saldo"] += cena * ilosc
            save_sprzedaz(akcja, produkt, cena, ilosc)

        elif akcja == "stop":
            stop(akcja)
            break

print(konto)
print(magazyn)
# wrapper(sys.argv[1], konto, magazyn)
