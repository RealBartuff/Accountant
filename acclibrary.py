
"""class Zakup:
    def __init__(self, produkt, kwota, ilosc):
        self.type = "zakup"
        self.produkt = produkt
        self.kwota = int(kwota)
        self.ilosc = int(ilosc)

    def write(self):
        print("{} \n{} \n{} \n{}".format(self.type, self.produkt, self.kwota, self.ilosc))


class Sprzedaz:
    def __init__(self, produkt, kwota, ilosc):
        self.type = "sprzedaz"
        self.produkt = produkt
        self.kwota = int(kwota)
        self.ilosc = int(ilosc)

    def write(self):
        print("{} \n{} \n{} \n{}".format(self.type, self.produkt, self.kwota, self.ilosc))"""


def save_saldo(akcja, operacja, comment):
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

def stop(akcja):
    current_data = open("out.txt", "a")
    print("stop")
    current_data.write(str(akcja) + "\n")
    current_data.close()

# def wrapper(konto, magazyn):