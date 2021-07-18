import sys

from acclibrary import Manager

magazyn = Manager()

magazyn.load(sys.argv[1])
magazyn.balance(sys.argv[2], sys.argv[3])

magazyn.save_balance("saldo", sys.argv[2], sys.argv[3])
