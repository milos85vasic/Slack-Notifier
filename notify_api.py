from slackclient import SlackClient

from configuration import token
from configuration import user
from configuration import channel

sc = SlackClient(token)


def notify(message):
    sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=message,
        user=user
    )
