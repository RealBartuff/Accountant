

from acclibrary import save_saldo, save_zakup, save_sprzedaz, stop, wrapper, Magazyn

magazyn = Magazyn()
with open("in.txt") as data:


    while True:
        pozycja = data.tell()
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
            if towar[produkt] < ilosc:
                print("Niewystarczająca ilość sztuk.")
                break
            else:
                towar[produkt] -= ilosc
            konto["saldo"] += cena * ilosc
            save_sprzedaz(akcja, produkt, cena, ilosc)

        elif akcja == "stop":
            data.seek(pozycja)
            stop(akcja)
            break


wrapper(konto, magazyn, towar)


