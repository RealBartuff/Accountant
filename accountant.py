
import sys

stan_konta = 0
zmiana = 0
konto = {"saldo": stan_konta}
magazyn = {}
dane = []



while True:
    akcja = input().strip()
    if akcja == "saldo":
        zmiana = int(input())
        comment = str(input())
        if stan_konta + zmiana < 0:
            print("error")
            break
        stan_konta += zmiana
        konto["saldo"] =+ stan_konta
        dane.append(["saldo", zmiana, comment])

    elif akcja == "zakup":
        id_produkt = str(input())
        cena = int(input())
        sztuk = int(input())
        if (cena * sztuk) < konto["saldo"]:
            stan_konta =- cena * sztuk
            konto["saldo"] += stan_konta
            if id_produkt in magazyn:
                magazyn[id_produkt] += sztuk
            else:
                magazyn[id_produkt] = sztuk
            dane.append(["zakup", id_produkt, cena, sztuk])
        if cena < 0 or sztuk <= 0:
            print("Podano nieprawidłowe wartości.")
            break

    elif akcja == "sprzedaz":
        id_produkt = str(input())
        cena = int(input())
        sztuk = int(input())
        if id_produkt in magazyn:
            magazyn[id_produkt] -= sztuk
            stan_konta = + cena * sztuk
            konto["saldo"] += stan_konta
            dane.append(["sprzedaz", id_produkt, cena, sztuk])
        elif id_produkt not in magazyn:
            print("Brak produktu w magazynie")
            break


    elif akcja == "stop":
        # print("stop")
        break


if sys.argv[1] == "sprzedaz":
    id_produkt = sys.argv[2]
    cena = int(sys.argv[3])
    sztuk = int(sys.argv[4])
    if id_produkt in magazyn:
        stan_konta = + cena * sztuk
        konto["saldo"] += stan_konta
        dane.append([sys.argv[1], id_produkt, cena, sztuk])
        magazyn[id_produkt] -= sztuk
    else:
        print("Brak towaru w magazynie!")
    for lista in dane:
        for item in lista:
            print(item)
    print("stop")

if sys.argv[1] == "zakup":
    id_produkt = sys.argv[2]
    cena = int(sys.argv[3])
    sztuk = int(sys.argv[4])
    if (cena * sztuk) < konto["saldo"]:
        stan_konta = - cena * sztuk
        konto["saldo"] += stan_konta
        if id_produkt in magazyn:
            magazyn[id_produkt] += sztuk
        else:
            magazyn[id_produkt] = sztuk
        dane.append(["zakup", id_produkt, cena, sztuk])
    if cena < 0 or sztuk <= 0:
        print("Podano nieprawidłowe wartości.")
    for lista in dane:
        for item in lista:
            print(item)
    print("stop")

if sys.argv[1] == "magazyn":
    id_produkt = str(sys.argv[4])
    sztuk = 0
    if id_produkt not in magazyn:
        magazyn[id_produkt] = sztuk
    if id_produkt in magazyn:
        for produkt, ilosc in magazyn.items():
            print("{}: {}".format(produkt, ilosc))

if sys.argv[1] == "saldo":
    print(konto["saldo"])

if sys.argv[1] == "konto":
    print(konto["saldo"])

if sys.argv[1] == "przeglad":
    start = 0
    koniec = 0
    if len(sys.argv) > 2:
        start = sys.argv[2]
        koniec = sys.argv[3]
    for lista in dane[int(start):int(koniec)]:
        for item in lista:
            print(item)
    print("stop")
