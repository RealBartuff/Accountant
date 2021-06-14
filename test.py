
import sys

from acclibrary import Saldo, Zakup, Sprzedaz

current_data = open("out.txt", "w")
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
            current_data.write(str(akcja) + "\n")
            current_data.write(str(operacja)+"\n")
            current_data.write(str(comment) + "\n")

        elif akcja == "zakup":
            produkt = data.readline().rstrip()
            cena = data.readline().rstrip()
            ilosc = data.readline().rstrip()
            magazyn[akcja] = Zakup(produkt, cena, ilosc)
            for k, v in magazyn.items():
                v.write()
            current_data.write(str(akcja) + "\n")
            current_data.write(str(produkt)+"\n")
            current_data.write(str(cena) + "\n")
            current_data.write(str(ilosc) + "\n")

        elif akcja == "sprzedaz":
            produkt = data.readline().rstrip()
            cena = data.readline().rstrip()
            ilosc = data.readline().rstrip()
            magazyn[akcja] = Sprzedaz(produkt, cena, ilosc)
            for k, v in magazyn.items():
                v.write()
            current_data.write(str(akcja) + "\n")
            current_data.write(str(produkt)+"\n")
            current_data.write(str(cena) + "\n")
            current_data.write(str(ilosc) + "\n")

        elif akcja == "stop":
            print("stop")
            current_data.write(str(akcja) + "\n")
            break

current_data.close()