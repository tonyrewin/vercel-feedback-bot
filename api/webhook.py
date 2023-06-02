from sanic import Sanic
from sanic.response import text
from tgbot.config import WEBHOOK, FEEDBACK_CHAT_ID
from tgbot.handlers.handle_feedback import handle_feedback, handle_answer
from tgbot.handlers.handle_filter import handle_filter
from tgbot.api import register_webhook, send_message


app = Sanic(name="belbekmarket-bot")
app.config.REGISTERED = False


@app.route('/', methods=["GET"])
async def register(req):
    res = 'skipped'
    if not app.config.REGISTERED:
        r = register_webhook(WEBHOOK)
        print(f'\n\t\t\tWEBHOOK REGISTERED:\n{r}')
        app.config.REGISTERED = True
        print(r)
        res = 'ok'
    return text(res)

@app.post('/')
async def handle(req):
    print(req)
    try:
        update = req.json
        print(update)
        msg = update.get('message', update.get('edited_message'))
        if msg:
            if 'text' in msg:
                if msg['chat']['id'] == msg['from']['id']:
                    handle_feedback(msg)
                elif str(msg['chat']['id']) == FEEDBACK_CHAT_ID:
                    if 'reply_to_message' in msg:
                        handle_answer(msg)
                else:
                    handle_filter(msg)
    
    except Exception:
        import traceback
        r = send_message(FEEDBACK_CHAT_ID, f'<pre>{traceback.format_exc()}</pre>')
        traceback.print_exc()
    return text('ok')
