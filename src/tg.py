"""
Телеграм бот для обработки текста с помощью Gradio.
"""

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '6335769743:AAEqgEVwH9J_ZsEvir5NIWB98uWRviN49JA'
# Замените 'HOST PORT' на данные где запущен Gradio
HOST = '127.0.0.1'
PORT = '7860'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обработчик команды /start
    :param update:
    :param context:
    :return:
    """
    message = ''
    message += f'Привет {update.effective_user.first_name}\n'
    message += 'Это бот для помощи студентам с конспектами\n'
    message += 'Введите текст, который хотите обработать'

    await update.message.reply_text(message)


async def response_to_gradio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Обработчик текста. Отправляет текст в Gradio и возвращает результат.
    :param update:
    :param context:
    :return:
    """
    response = requests.post(f"http://{HOST}:{PORT}/run/predict", json={
        "data": [
            update.message.text,
            50,
            250,
        ]
    }).json()
    message = f'{response["data"]} \nВремя обработки запроса {response["duration"]}'

    await update.message.reply_html(message)


if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()  # Создаем приложение
    app.add_handler(CommandHandler("start", start, ~filters.ChatType.GROUP))  # Добавляем обработчик команды /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, response_to_gradio))  # Добавляем обработчик текста

    app.run_polling()  # Запускаем приложение
