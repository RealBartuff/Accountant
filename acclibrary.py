
class Saldo:
    def __init__(self, kwota, komentarz):
        self.type = "saldo"
        self.kwota = int(kwota)
        self.komentarz = komentarz

    def write(self):
        print("{} \n{} \n{}".format(self.type, self.kwota, self.komentarz))


class Zakup:
    def __init__(self, produkt, kwota, ilosc):
        self.type = "zakup"
        self.produkt = produkt
        self.kwota = kwota
        self.ilosc = ilosc

    def write(self):
        print("{} \n{} \n{} \n{}".format(self.type, self.produkt, self.kwota, self.ilosc))


class Sprzedaz:
    def __init__(self, produkt, kwota, ilosc):
        self.type = "sprzedaz"
        self.produkt = produkt
        self.kwota = kwota
        self.ilosc = ilosc

    def write(self):
        print("{} \n{} \n{} \n{}".format(self.type, self.produkt, self.kwota, self.ilosc))
