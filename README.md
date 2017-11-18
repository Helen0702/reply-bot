# Telegram Reply Bot

This is a telegram bot that will reply to messages when certain keywords are picked up in a group chat. It uses the Flask web framework and the Telegram Bot API to get chat updates via webhooks.

Dependencies: telepot, flask
___

### How To Use

After cloning the project from GitHub, you will need to create bot_details.py:

```
def get_botID(bot_name):
    if bot_name == '<YOUR_BOT_NAME>':
        return '<YOUR_BOT_KEY>'

def get_serverURL():
    return "<YOUR_SERVER_URL>"
```

`<YOUR_BOT_KEY>` is the one privided by BotFather and `<YOUR_SERVER_URL>` is the URL used to connect to the server. 