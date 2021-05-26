
import sys

saldo = 0
stan_magazyn = 0
ilosc_magazyn = 0
dane = []

while True:
    if sys.argv[1] == "saldo":
        saldo = int(input())  #saldo chyba powinno byc float
        comment = str(input())
        dane.append("saldo")
        dane.append(saldo)
        dane.append(comment)
        print("saldo: {}, komentarz: {}".format(saldo, comment))

    if sys.argv[1] == "sprzedaz":
        produkt = str(sys.argv[2])
        cena = int(sys.argv[3])
        sztuk = int(sys.argv[4])
        dane.append("sprzedaz")
        dane.append(produkt)
        dane.append(cena)
        dane.append(sztuk)
        print("produkt: {}, cena za szt.: {}, sprzedano sztuk: {}".format(produkt, cena, sztuk))

    if sys.argv[1] == "zakup":
        produkt = str(sys.argv[2])
        cena = int(sys.argv[3])
        sztuk = int(sys.argv[4])
        if (cena * sztuk) < saldo:
            dane.append("zakup")
            dane.append(produkt)
            dane.append(cena)
            dane.append(sztuk)
            saldo -= cena * sztuk
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

print(saldo)
