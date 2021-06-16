
class Magazyn:
    def __init__(self):
        self.konto = 0
        self.produkty = {}
        self.historia = []

    def saldo(self, wartosc, comment):
        if self.konto + int(wartosc) < 0:
            print("Niewystarczające środki na koncie.")
            return False
        self.konto += int(wartosc)
        self.historia.append(["saldo", wartosc, comment])
        return True

    def zakup(self, produkt, wartosc, ilosc):
        if self.konto < wartosc * ilosc:
            print("Niewystarczające środki na koncie.")
            return False
        else:
            self.konto -= wartosc * ilosc
        self.produkty[produkt] = + ilosc
        self.historia.append(["zakup", produkt, wartosc, ilosc])
        return True

    def sprzedaz(self, produkt, wartosc, ilosc):
        if produkt not in self.produkty:
            print("Brak towaru w magazynie.")
            return False
        if self.produkty[produkt] < ilosc:
            print("Niewystarczająca ilość sztuk.")
            return False
        else:
            self.produkty[produkt] -= ilosc
        self.konto += wartosc * ilosc
        self.historia.append(["sprzedaz", produkt, wartosc, ilosc])
        return True

    def wczytaj(self, data):
        magazyn = Magazyn()
        with open(sys.argv[1]) as data:

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
                    magazyn.zakup(produkt, cena, ilosc)

                elif akcja == "sprzedaz":
                    produkt = str(data.readline().rstrip())
                    cena = int(data.readline().rstrip())
                    ilosc = int(data.readline().rstrip())
                    magazyn.sprzedaz(produkt, cena, ilosc)

                elif akcja == "stop":
                    data.seek(pozycja)
                    stop(akcja)
                    break

    def zapisz(self, akcja, operacja, comment):
        current_data = open("in.txt", "a")
        current_data.write(str(akcja) + "\n")
        current_data.write(str(operacja) + "\n")
        current_data.write(str(comment) + "\n")
        current_data.close()


import sys

"""def save_saldo(akcja, operacja, comment):
    current_data = open("out.txt", "a")
    current_data.write(str(akcja) + "\n")
    current_data.write(str(operacja) + "\n")
    current_data.write(str(comment) + "\n")
    current_data.close()

def save_zakup(akcja, produkt, cena, ilosc):
    current_data = open("out.txt", "a")
    current_data.write(str(akcja) + "\n")
    current_data.write(str(produkt)+"\n")
    current_data.write(str(cena) + "\n")
    current_data.write(str(ilosc) + "\n")
    current_data.close()

def save_sprzedaz(akcja, produkt, cena, ilosc):
    current_data = open("out.txt", "a")
    current_data.write(str(akcja) + "\n")
    current_data.write(str(produkt) + "\n")
    current_data.write(str(cena) + "\n")
    current_data.write(str(ilosc) + "\n")
    current_data.close()

"""
def stop(akcja):
    current_data = open("out.txt", "a")
    current_data.write(str(akcja) + "\n")
    current_data.close()
    """

def p_konto(konto):
    for saldo, suma in konto.items():
        print(suma)
        break

def p_saldo(akcja, konto):
    operacja = int(sys.argv[2])
    comment = str(sys.argv[3])
    if konto["saldo"] + operacja < 0:
        return ("Niewystarczające środki na koncie.")
    konto["saldo"] += operacja
    save_saldo(akcja, operacja, comment)

def p_zakup(akcja, konto, magazyn):
    produkt = str(sys.argv[2])
    cena = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    if konto["saldo"] < cena * ilosc:
        return ("Niewystarczające środki na koncie.")
    else:
        konto["saldo"] -= cena * ilosc
    towar = {}
    towar[produkt] = + ilosc
    magazyn.append(towar)
    save_zakup(akcja, produkt, cena, ilosc)

def p_sprzedaz(akcja, konto, towar):
    produkt = str(sys.argv[2])
    cena = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    if produkt not in towar:
        return ("Brak towaru w magazynie.")
    if towar[produkt] < ilosc:
        return ("Niewystarczająca ilość sztuk.")
    else:
        towar[produkt] -= ilosc
    konto["saldo"] += cena * ilosc
    save_sprzedaz(akcja, produkt, cena, ilosc)


def wrapper(konto, magazyn, towar):
    akcja = sys.argv[1]
    while akcja:
        if akcja == "konto":
            p_konto(konto)
            break

        if akcja == "saldo":
            p_saldo(akcja, konto)
            break

        if akcja == "zakup":
            p_zakup(akcja, konto, magazyn)
            break

        if akcja == "sprzedaz":
            p_sprzedaz(akcja, konto, towar)
            break
"""


"""if sys.argv[1] == "sprzedaz":
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
        id_produkt = str(sys.argv[2:])
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
        print("stop")"""