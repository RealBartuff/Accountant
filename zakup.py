import sys

from accountant import manager


manager.process()
manager.process_action("zakup", sys.argv[1:])
