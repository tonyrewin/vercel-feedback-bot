import requests
import json
import os

TOKEN = os.environ.get('BOT_TOKEN')
apiBase = f"https://api.telegram.org/bot{TOKEN}/"


def register_webhook(url):
    r = requests.get(
        apiBase + f'setWebhook?url={url}'
    )
    return r.json()


# https://core.telegram.org/bots/api#deletemessage
def delete_message(cid: str, mid: str):
    url = apiBase + f"deleteMessage?chat_id={cid}&message_id={mid}"
    r = requests.post(url)
    return r.json()


# https://core.telegram.org/bots/api#sendmessage
def send_message(cid: str, body, reply_to=None, reply_markup=None):
    url = apiBase + f"sendMessage?chat_id={cid}&text={body}"
    if reply_to:
        url += f'&reply_to_message_id={reply_to}'
    if reply_markup:
        reply_markup = json.dumps(reply_markup)
        reply_markup = requests.utils.quote(reply_markup)
        url += f'&reply_markup={reply_markup}'
    url += f'&parse_mode=HTML'
    r = requests.post(url)
    print(f'{url}')
    return r.json()


# https://core.telegram.org/bots/api#forwardmessage
def forward_message(cid, mid, to_chat_id):
    url = apiBase + f"forwardMessage?chat_id={to_chat_id}" + \
        f"&from_chat_id={cid}&message_id={mid}"
    r = requests.post(url)
    return r.json()


# https://core.telegram.org/bots/api#banchatmember
def erase_member(chat_id, member_id):
    url = f"banChatSenderChat?chat_id={cid}&user_id={member_id}&revoke_messages=1"
    r = requests.post(apiBase + url)
    print(r.json())
    return r.json()