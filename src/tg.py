from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '6335769743:AAEqgEVwH9J_ZsEvir5NIWB98uWRviN49JA'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = ''
    message += f'Привет {update.effective_user.first_name}\n'
    message += 'Это бот для помощи студентам с конспектами\n'
    message += 'Чтобы воспользоваться нейронкой воспользуйтесь командой /summ'

    await update.message.reply_text(message)


async def summ(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Хаха попался')
    

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("summ", summ))

app.run_polling()