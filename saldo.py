import sys

from manager import Reader, Manager, Writer

reader = Reader("in.txt")
manager = Manager(reader)
writer = Writer("in.txt", "out.txt")


@manager.action("saldo", 2)
def saldo(manager, rows):
    price = float(rows[0])
    manager.modify_account(price)


@manager.action("zakup", 3)
def zakup(manager, rows):
    name = rows[0]
    price = float(rows[1])
    qty = float(rows[2])
    manager.modify_account(-price*qty)
    manager.modify_stock(name, qty)


@manager.action("sprzedaz", 3)
def sprzedaz(manager, rows):
    name = rows[0]
    price = float(rows[1])
    qty = float(rows[2])
    manager.modify_account(price*qty)
    manager.modify_stock(name, -qty)


manager.process()
manager.process_action("saldo", sys.argv[1:])
