import sys

from acclibrary import Magazyn

magazyn = Magazyn()

magazyn.wczytaj(sys.argv[1])
magazyn.przeglad(sys.argv[2], sys.argv[3])
