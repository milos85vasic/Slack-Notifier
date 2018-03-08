import sys

from notify_api import notify

message = ""

for arg in sys.argv:
    if sys.argv.index(arg) > 0:
        message += arg + "\n"

notify(message)
