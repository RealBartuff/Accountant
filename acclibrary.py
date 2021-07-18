
class Manager:
    def __init__(self):
        self.account = 0
        self.products = {}
        self.history = []

    def balance(self, value, comment):
        if self.account + int(value) < 0:
            print("Niewystarczające środki na koncie.")
            return False
        self.account += int(value)
        self.history.append(["saldo", value, comment])
        return True

    def purchase(self, product, value, quantity):
        if self.account < int(value) * int(quantity):
            print("Niewystarczające środki na koncie.")
            return False
        self.account -= int(value) * int(quantity)
        self.products[product] = + int(value)
        self.history.append(["zakup", product, value, quantity])
        return True

    def sale(self, product, value, quantity):
        if product not in self.products:
            print("Brak towaru w magazynie.")
            return False
        if self.products[product] < quantity:
            print("Niewystarczająca ilość sztuk.")
            return False
        else:
            self.products[product] -= quantity
        self.account += int(value) * int(quantity)
        self.history.append(["sprzedaz", product, value, quantity])
        return True

    def wczytaj(self, typ):
        with open(typ) as data:
            while True:
                akcja = data.readline().rstrip()
                if not akcja:
                    break

                elif akcja == "saldo":
                    operacja = int(data.readline().rstrip())
                    comment = data.readline().rstrip()
                    self.saldo(operacja, comment)

                elif akcja == "zakup":
                    produkt = str(data.readline().rstrip())
                    cena = int(data.readline().rstrip())
                    ilosc = int(data.readline().rstrip())
                    self.zakup(produkt, cena, ilosc)

                elif akcja == "sprzedaz":
                    produkt = str(data.readline().rstrip())
                    cena = int(data.readline().rstrip())
                    ilosc = int(data.readline().rstrip())
                    self.sprzedaz(produkt, cena, ilosc)

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
        for lista in self.historia[int(start): int(koniec)]:
            for item in lista:
                print(item)

    def magazyn(self, produkt):
        for item in produkt:
            if item not in self.produkty:
                self.produkty[item] = 0
        for produkt, ilosc in self.produkty.items():
            print("{}: {}".format(produkt, ilosc))
