
import sys

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
        if self.konto < int(wartosc) * int(ilosc):
            print("Niewystarczające środki na koncie.")
            return False
        self.konto -= int(wartosc) * int(ilosc)
        self.produkty[produkt] = + int(ilosc)
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
        self.konto += int(wartosc) * int(ilosc)
        self.historia.append(["sprzedaz", produkt, wartosc, ilosc])
        return True

    def wczytaj(self, typ):
        magazyn = Magazyn()
        with open(typ) as data:
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

    def zapisz_saldo(self, akcja, operacja, comment):
        with open("in.txt", "r") as dane:
            contents = dane.readlines()
            contents.insert(-1, (str(akcja) + "\n"))
            contents.insert(-1, (str(operacja) + "\n"))
            contents.insert(-1, (str(comment) + "\n"))

        with open("in.txt", "w") as dane:
            contents = "".join(contents)
            dane.write(contents)

    def zapisz_zs(self, akcja, produkt, cena, ilosc):
        with open("in.txt", "r") as dane:
            contents = dane.readlines()
            contents.insert(-1, (str(akcja) + "\n"))
            contents.insert(-1, (str(produkt) + "\n"))
            contents.insert(-1, (str(cena) + "\n"))
            contents.insert(-1, (str(ilosc) + "\n"))

        with open("in.txt", "w") as dane:
            contents = "".join(contents)
            dane.write(contents)

    def przeglad(self, start, koniec):
        magazyn = Magazyn()
        for lista in magazyn.historia[int(start):int(koniec)]:
            for item in lista:
                print(item)
                print("stop")
