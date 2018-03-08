import sys

from notify_api import notify

message = ""

for line in sys.stdin:
    message += line + "\n"

notify(message)
