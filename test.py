
import sys
"""
stan_konta = 0
zmiana = 0
konto = {"saldo": stan_konta}
magazyn = {}
dane = []
sztuk = 0


while True:
    akcja = input().strip() or sys.argv[1]
    if akcja == "saldo":
        zmiana = int(input()) or sys.argv[2]
        comment = str(input()) or sys.argv[3]
        if stan_konta + zmiana < 0:
            print("error")
            break
        stan_konta += zmiana
        konto["saldo"] =+ stan_konta
        dane.append([akcja, zmiana, comment])

    elif akcja == "zakup":
        id_produkt = str(input()) or sys.argv[2]
        cena = int(input()) or sys.argv[3]
        sztuk = int(input()) or sys.argv[4]
        if (cena * sztuk) < konto["saldo"]:
            stan_konta =- cena * sztuk
            konto["saldo"] += stan_konta
            # magazyn.append([id_produkt, sztuk])
            if id_produkt in magazyn:
                magazyn[id_produkt] += sztuk
            else:
                magazyn[id_produkt] = sztuk
            dane.append([akcja, id_produkt, cena, sztuk])
            print(magazyn)
        if cena < 0 or sztuk <= 0:
            print("Podano nieprawidłowe wartości.")
            break

    elif akcja == "sprzedaz":
        id_produkt = str(input()) or sys.argv[2]
        cena = int(input()) or sys.argv[3]
        sztuk = int(input()) or sys.argv[4]
        if [id_produkt, sztuk] in magazyn:
            magazyn.remove([id_produkt, sztuk])
            stan_konta =+ cena * sztuk
            konto["saldo"] += stan_konta
            dane.append([akcja, id_produkt, cena, sztuk])
            print(magazyn)
            for lista in dane:                                          # wyświetlanie pliku in.txt
                for element in lista:
                    print(element)
            # print(sys.argv[2])                                          # dodawanie sysów do pliku txt
            # print(sys.argv[3])
            # print(sys.argv[4])

    elif sys.argv[1] == "saldo":
        print(konto["saldo"])
        break

    elif sys.argv[1] == "konto":
        print(konto["saldo"])
        break

    elif sys.argv[1] == "przeglad":
        for lista in dane:
            for item in lista:
                print(item)
        print("stop")
        break

    elif sys.argv[1] == "magazyn":
        for id_produkt in sys.argv[2:]:
            if id_produkt in magazyn:
                stan_magazynu = magazyn[sztuk]
            else:
                stan_magazynu = 0
            print(magazyn)
            print(id_produkt, ":", stan_magazynu)
        break

    elif akcja == "stop":
        print("stop")
        break
"""
if sys.argv[1] == "magazyn":
    item = str(sys.argv)
    for produkt, ilosc in magazyn.items():
        if produkt in magazyn:
            print("{}: {}".format(item, ilosc))
        if produkt not in magazyn:
            print(item, ":", 0)