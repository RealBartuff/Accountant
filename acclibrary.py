
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

    def sale(self, product, value, qty):
        if product not in self.products:
            print("Brak towaru w magazynie.")
            return False
        if self.products[product] < qty:
            print("Niewystarczająca ilość sztuk.")
            return False
        else:
            self.products[product] -= qty
        self.account += int(value) * int(qty)
        self.history.append(["sprzedaz", product, value, qty])
        return True

    def load(self, typ):
        with open(typ) as data:
            while True:
                action = data.readline().rstrip()
                if not action:
                    break

                elif action == "saldo":
                    operation = int(data.readline().rstrip())
                    comment = data.readline().rstrip()
                    self.balance(operation, comment)

                elif action == "zakup":
                    product = str(data.readline().rstrip())
                    price = int(data.readline().rstrip())
                    qty = int(data.readline().rstrip())
                    self.purchase(product, price, qty)

                elif action == "sprzedaz":
                    product = str(data.readline().rstrip())
                    price = int(data.readline().rstrip())
                    qty = int(data.readline().rstrip())
                    self.sale(product, price, qty)

                elif action == "stop":
                    break

    def save_saldo(self, action, operation, comment):
        with open("in.txt", "r") as dane:
            contents = dane.readlines()
            contents.insert(-1, (str(action) + "\n"))
            contents.insert(-1, (str(operation) + "\n"))
            contents.insert(-1, (str(comment) + "\n"))

        with open("in.txt", "w") as dane:
            contents = "".join(contents)
            dane.write(contents)

    def save_purchase_sale(self, action, product, price, qty):
        with open("in.txt", "r") as dane:
            contents = dane.readlines()
            contents.insert(-1, (str(action) + "\n"))
            contents.insert(-1, (str(product) + "\n"))
            contents.insert(-1, (str(price) + "\n"))
            contents.insert(-1, (str(qty) + "\n"))

        with open("in.txt", "w") as dane:
            contents = "".join(contents)
            dane.write(contents)

    def review(self, start, end):
        for lista in self.history[int(start): int(end)]:
            for item in lista:
                print(item)

    def magazyn(self, product):
        for item in product:
            if item not in self.products:
                self.products[item] = 0
        for product, qty in self.products.items():
            print("{}: {}".format(product, qty))
