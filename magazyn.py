import sys

import accountant
from accountant import manager


manager.process()
manager.process_action("magazyn", sys.argv[1:])
