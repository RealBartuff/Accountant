import sys

from accountant import manager


manager.process()
manager.process_action("przeglad", sys.argv[1:])
