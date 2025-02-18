import os
from pyrogram import Client, filters
import openai
import logging

# Настройки
API_ID = *  # API ID Telegram
API_HASH = ""  # API Hash Telegram
SESSION_STRING = ""  # Строка сессии Telegram
PROXYAPI_KEY = ""  # API ProxyAPI
PROXYAPI_BASE_URL = "https://api.proxyapi.ru/openai/v1"  # URL ProxyAPI
# Конец настроек

openai.api_key = PROXYAPI_KEY
openai.api_base = PROXYAPI_BASE_URL

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Client(
    "my_account",
    session_string=SESSION_STRING,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.private)
async def chat_handler(client, message):
    try:
        if message.from_user.id == (await client.get_me()).id:
            logging.info("Сообщение от самого аккаунта игнорируется.")
            return

        print(f"Получено сообщение от {message.from_user.id}: {message.text}")
        logging.info(f"Получено сообщение от {message.from_user.id}: {message.text}")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.text},
            ]
        )

        reply = response.choices[0].message["content"]

        await message.reply_text(reply)
        print(f"Ответ {message.from_user.id}: {reply}")
        logging.info(f"Ответ {message.from_user.id}: {reply}")

    except Exception as e:
        print(f"Ошибка в обработке: {e}")
        logging.error(f"Ошибка в обработке: {e}")
        await message.reply_text("Произошла ошибка. Попробуйте позже.")

if __name__ == "__main__":
    try:
        print("Запуск")
        app.run()
    except Exception as e:
        print(f"Ошибка запуска: {e}")
        logging.error(f"Ошибка запуска: {e}")
