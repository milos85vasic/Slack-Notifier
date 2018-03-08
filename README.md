# Slack Notifier

Send messages to choose channels. Used mainly as tool for reporting.

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