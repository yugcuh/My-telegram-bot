import telebot
import os

BOT_TOKEN = os.getenv("7659107814:AAGr4PQm1ji7JaWsey-n9cLTY5HuhJzNhTQ")
ADMIN_ID = 7031398615  # ← ضع ID حسابك هنا

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    if message.from_user.id != ADMIN_ID:
        bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
        bot.reply_to(message, "✅ تم إرسال رسالتك، سيتم الرد عليك قريبًا.")
    else:
        if message.reply_to_message:
            bot.send_message(
                message.reply_to_message.forward_from.id,
                message.text
            )

bot.infinity_polling()