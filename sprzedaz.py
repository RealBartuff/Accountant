import sys

from accountant import manager


manager.process()
manager.process_action("sprzedaz", sys.argv[1:])
manager.save()
