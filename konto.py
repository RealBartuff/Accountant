import sys

from acclibrary import Manager

magazyn = Manager()
magazyn.load(sys.argv[1])

print(magazyn.account)
