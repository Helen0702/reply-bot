import telepot
from flask import Flask, request
import urllib3
from .bot_details import get_botID, get_serverURL

### NEEDED FOR PYTHONANYWHERE DEPLOYMENT - uncomment if using pythonanywhere ###
# proxy_url = "http://proxy.server:3128"
# telepot.api._pools = {
#     'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
# }
# telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
### END ###

bot = telepot.Bot(get_botID('althea'))
bot.setWebhook(get_serverURL(), max_connections=40)
app = Flask(__name__)

@app.route('/', methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        manage_message(update["message"])
    return "OK"

# handles the message grabbed from the update
def manage_message(message):
    if "text" in message:
        reply_message(message)
    return

# replies message
def reply_message(message):
    text = message["text"].lower()
    chat = message["chat"]
    chat_id = chat["id"]
    user = message["from"]
    if chat["type"] in ["group", "supergroup"]:
        if is_not_admin(user, chat_id):
            if 'telegram handle' in text:
                reply = """You need a unique telegram handle, such as @oolala.
        To create a telegram handle, please go to Settings in your Telegram account and key in your username in the Username field."""
                bot.sendMessage(chat_id, text=reply, parse_mode="Markdown", reply_to_message_id=message["message_id"])
            elif 'when' in text and 'ico' in text.split():
                reply = """Pre-sale will start on 27 Nov and public sale in early Dec. Whitelist details will be out soon!"""
                bot.sendMessage(chat_id, text=reply, parse_mode="Markdown", reply_to_message_id=message["message_id"])
            elif 'respond' in text and 'bot' in text.split():
                reply = """As we are currently experiencing a influx of submissions for the bounty, please be patient when interacting with @olympuslabsbot to submit your entry. There is still a lot of time before our ICO so there is no rush."""
                bot.sendMessage(chat_id, text=reply, parse_mode="Markdown", reply_to_message_id=message["message_id"])
    if chat["type"] == "private":
        reply = """Sorry! I don't talk to people in private chats :( """
        bot.sendMessage(chat_id, text=reply, parse_mode="Markdown")
    return

# returns True if user is not admin in chat_id
def is_not_admin(user, chat_id):
    chat_mem_arr = bot.getChatAdministrators(chat_id)
    for chat_mem in chat_mem_arr:
        if chat_mem["user"] == user:
            return False
    return True
