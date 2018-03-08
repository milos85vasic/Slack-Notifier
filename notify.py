import sys

from notify_api import notify

message = ""

for arg in sys.argv:
    message += arg + "\n"

notify(message)
