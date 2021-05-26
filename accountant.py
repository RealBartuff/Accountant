#TODO:
# "Program zapamiętuje każdą wprowadzoną linię",
# "Program wraca do kroku I",
# a) b) c) program dodaje do historii podane argumenty tak jakby miały być wprowadzone przez standardowe wejście, przechodzi do kroku V
# d) program wypisuje na standardowe wyjście stan konta po wszystkich akcjach, kończy działanie
# e) program wypisuje stany magazynowe dla podanych produktów, w formacie: <id produktu>: <stan> w nowych liniach i kończy działanie:
# f) Program wypisuje wszystkie akcje zapisane pod indeksami w zakresie [od, do] (zakresy włącznie)
# V. Program wypisuje wszystkie podane parametry w formie identycznej w jakiej je pobrał

import sys

srodki = 0
stan_magazyn = 0
ilosc_magazyn = 0
dane = []

while True:
    if sys.argv[1] == "saldo":
        saldo = str(input())
        srodki = int(input())       #srodki chyba powinno byc float
        comment = str(input())
        dane.append([saldo, srodki, comment])       #insert?
        print("saldo: {}, komentarz: {}".format(srodki, comment))

    if sys.argv[1] == "sprzedaz":
        produkt = str(sys.argv[2])
        cena = int(sys.argv[3])
        sztuk = int(sys.argv[4])
        dane.append([input(), produkt, cena, sztuk])
        print("produkt: {}, cena za szt.: {}, sprzedano sztuk: {}".format(produkt, cena, sztuk))

    if sys.argv[1] == "zakup":
        produkt = str(sys.argv[2])
        cena = int(sys.argv[3])
        sztuk = int(sys.argv[4])
        if (cena * sztuk) < srodki:
            dane.append([input(), produkt, cena, sztuk])
            srodki -= cena * sztuk
            stan_magazyn += produkt
            ilosc_magazyn += sztuk
            print("produkt: {}, cena za szt.: {}, kupiono sztuk: {}".format(produkt, cena, sztuk))
        elif cena < 0:
            print("Nieprawidłowa wartość ceny.")
            break
        elif sztuk <= 0:
            print("Nieprawidłowa ilość sztuk")
            break
        else:
            print("Niewystarczające środki na koncie.")
            break
    else:
        print("ERROR! Podano nieprawidłowe wartości.")
        break

print(dane)
