import redis
from tgbot.config import REDIS_URL

# сохраняет сессии, айди кнопок в чатах для удаления и пересылаемые сообщения между перезагрузками
storage = redis.from_url(REDIS_URL)