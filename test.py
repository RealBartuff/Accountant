
# import sys

stan_konta = 0
zmiana = 0
konto = {"saldo": stan_konta}
id_produkt = str()
cena = 0
sztuk = 0
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
        print(konto)

    elif akcja == "zakup":
        id_produkt = str(input())
        cena = int(input())
        sztuk = int(input())
        if cena < 0 or sztuk <= 0:
            print("Podano nieprawidłowe wartości.")
            break
        elif (cena * sztuk) < stan_konta:
            stan_konta =- cena * sztuk
            ilosc_magazyn += sztuk
            konto["saldo"] += stan_konta
            magazyn.append(id_produkt)
            magazyn.append(ilosc_magazyn)
            dane.append([akcja, id_produkt, cena, sztuk])
        print(konto["saldo"])
        print(dane)

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
        print(konto)
        
# while True:
#     if sys.argv[1] == "saldo":
#         print(konto["saldo"])
#         pass
#
#     elif sys.argv[1] == "zakup":
#         dane.append([sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]])
#         for wpis in dane:
#             for element in wpis:
#                 print(element)
#         print("stop")
#
#     elif sys.argv[1] == "sprzedaz":
#         dane.append([sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]])
#         for wpis in dane:
#             for element in wpis:
#                 print(element)
#         print("stop")
#
#     elif sys.argv[1] == "konto":
#         print(konto["saldo"])
#         break
#
#     elif sys.argv[1] == "przeglad":
#         for wpis in dane:
#             for element in wpis:
#                 print(element)
#         break
#
    elif akcja == "stop":
        # for wpis in dane:
        #     for element in wpis:
        #                 print(element)
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