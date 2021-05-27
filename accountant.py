#TODO:
# "Program zapamiętuje każdą wprowadzoną linię",
# "Program wraca do kroku I",
# a) b) c) program dodaje do historii podane argumenty tak jakby miały być wprowadzone przez standardowe wejście, przechodzi do kroku V
# d) program wypisuje na standardowe wyjście stan konta po wszystkich akcjach, kończy działanie
# e) program wypisuje stany magazynowe dla podanych produktów, w formacie: <id produktu>: <stan> w nowych liniach i kończy działanie:
# f) Program wypisuje wszystkie akcje zapisane pod indeksami w zakresie [od, do] (zakresy włącznie)
# V. Program wypisuje wszystkie podane parametry w formie identycznej w jakiej je pobrał

import sys

stan_konta = 0
srodki = 0
id_produkt = []
ilosc_magazyn = 0
magazyn = {"produkt": id_produkt, "stan": ilosc_magazyn}
dane = []




while True:
    akcja = input().strip()
    if akcja == "saldo":
        srodki = int(input())
        comment = str(input())
        if stan_konta + srodki < 0:
            print("error")
            break
        dane.append([akcja, srodki, comment])
        stan_konta += srodki
        print("środki: {}, komentarz: {}".format(srodki, comment))
        print(stan_konta)
        # continue

    akcja = input().strip()
    if akcja == "zakup":
        id_produkt = str(input())
        cena = int(input())
        sztuk = int(input())
        if (cena * sztuk) < stan_konta:
            stan_konta =- cena * sztuk
            magazyn["produkt"] += id_produkt
            ilosc_magazyn += sztuk
            dane.append([akcja, id_produkt, cena, sztuk])
            print("produkt: {}, cena za szt.: {}, kupiono sztuk: {}".format(id_produkt, cena, sztuk))

        elif cena < 0 or sztuk <= 0:
            print("Podano nieprawidłowe wartości.")
            break
        else:
            print("Niewystarczające środki na koncie.")
            break
        continue

    if akcja == "magazyn":
        for id_produkt in sys.argv[2:]:
            if id_produkt in magazyn:
                stan_magazyn = magazyn[id_produkt]
            else:
                stan_magazyn = 0
            print("{}: ", "{}".format(id_produkt, stan_magazyn))
            break

    akcja = input().strip()
    if akcja == "sprzedaz":
        produkt = str(sys.argv[2])
        cena = int(sys.argv[3])
        sztuk = int(sys.argv[4])
        dane.append([input(), produkt, cena, sztuk])
        print("produkt: {}, cena za szt.: {}, sprzedano sztuk: {}".format(produkt, cena, sztuk))
        continue

    # else:
        # print("ERROR! Podano nieprawidłowe wartości.")
        # break





