import sys

from acclibrary import Magazyn

magazyn = Magazyn()
with open(sys.argv[1]) as data:
    while True:
        akcja = data.readline().rstrip()
        if not akcja:
            break

        elif akcja == "saldo":
            operacja = int(data.readline().rstrip())
            comment = data.readline().rstrip()
            magazyn.saldo(operacja, comment)

        elif akcja == "zakup":
            produkt = str(data.readline().rstrip())
            cena = int(data.readline().rstrip())
            ilosc = int(data.readline().rstrip())
            magazyn.zakup(produkt, cena, ilosc)

        elif akcja == "sprzedaz":
            produkt = str(data.readline().rstrip())
            cena = int(data.readline().rstrip())
            ilosc = int(data.readline().rstrip())
            magazyn.sprzedaz(produkt, cena, ilosc)

        elif akcja == "stop":
            break

print(magazyn.konto)
print(magazyn.historia)
print(magazyn.produkty)
