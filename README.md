# Slack Notifier

Send messages to choosen channels. Used mainly as tool for reporting.

## How to use

- Clone the project
- In project root create configuration.py with the following structure (as example):

```python
token = "your slack api token"
channel = "slack channel you use"
user = "your user"
```

- Run command:
```
$ python notify.py "This is a sample message."
```

- Or with pipeline:
```
$ some_command | python notify_pipe.py
```

## Dependencies

To be able to use Slack Notifier [Slack API](https://github.com/slackapi/python-slackclient) must be installed on the system.
