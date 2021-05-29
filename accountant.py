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
zmiana = 0
konto = {"saldo": stan_konta}
id_produkt = str()
ilosc_magazyn = 0
magazyn = []
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
        dane.append([akcja, zmiana, comment])
        print(akcja)
        print("środki: {}, komentarz: {}".format(zmiana, comment))
        # continue
    elif akcja == "zakup":
        id_produkt = str(input())
        cena = int(input())
        sztuk = int(input())
        if (cena * sztuk) < stan_konta:
            stan_konta =- cena * sztuk
            ilosc_magazyn += sztuk
            konto["saldo"] += stan_konta
            magazyn.append(id_produkt)
            magazyn.append(ilosc_magazyn)
            dane.append([akcja, id_produkt, cena, sztuk])
            print(akcja)
            print("produkt: {}, cena za szt.: {}, kupiono sztuk: {}".format(id_produkt, cena, sztuk))
        elif cena < 0 or sztuk <= 0:
            print("Podano nieprawidłowe wartości.")
            break
        else:
            print("Niewystarczające środki na koncie.")
            break
        # continue
    elif akcja == "sprzedaz":
        id_produkt = str(input())
        cena = int(input())
        sztuk = int(input())
        if id_produkt in magazyn and sztuk <= ilosc_magazyn:
            magazyn.remove(id_produkt)
            magazyn.remove(ilosc_magazyn)
            stan_konta =+ cena * sztuk
            konto["saldo"] += stan_konta
            dane.append([akcja, id_produkt, cena, sztuk])
        print(akcja)
        print("produkt: {}, cena za szt.: {}, sprzedano sztuk: {}".format(id_produkt, cena, sztuk))
        # continue
    elif akcja == "przeglad":
        for wpis in dane:
            for element in wpis:
                print(element)
        break
    elif sys.argv[1] == "saldoo":
        print(konto["saldo"])
        break
    elif akcja == "stop":
        print("Koniec programu.")
        break


    #
    # elif akcja == "magazyn":
    #     for id_produkt in sys.argv[2:]:
    #         if id_produkt in magazyn:
    #             stan_magazyn = magazyn[id_produkt]
    #         else:
    #             stan_magazyn = 0
    #         print("{}: ", "{}".format(id_produkt, stan_magazyn))
    #         break
    #

    # else:
        # print("ERROR! Podano nieprawidłowe wartości.")
        # break


    # akcja == sys.argv[1]
    # if akcja == "przeglad":
    #     for wpis in dane:
    #         for element in wpis:
    #             print(element)