import json

from tgbot.api import erase_member
from tgbot.storage import storage
from tgbot.config import FEEDBACK_CHAT_ID


stopwords = [
    'трейдинг'
]

def handle_feedback(msg):
    mid = msg['message_id']
    cid = msg['chat']['id']
    for sw in stopwords:
        if sw in msg['text']:
            erase_member()
