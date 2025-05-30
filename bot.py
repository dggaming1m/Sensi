import telebot
import json
import os

# ✅ Bot token
BOT_TOKEN = "8148398572:AAF1QepCMHy8WOW2NAamdAun0dEaGS5TiT4"  # Apna token yahan daalein
bot = telebot.TeleBot(BOT_TOKEN)

# ✅ Admin Telegram ID
ADMIN_ID = 5670174770  # Apna Telegram user ID daalein

# ✅ Sensitivity database load karo
if os.path.exists("sensitivity_database.json"):
    with open("sensitivity_database.json", "r") as f:
        sensitivity_data = json.load(f)
else:
    sensitivity_data = {}  # Agar file nahi mili to empty dict

# ✅ Start command
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(
        telebot.types.InlineKeyboardButton("Join channel ✅", url="https://t.me/dg_gaming_1m0")
    )
    markup.row(
        telebot.types.InlineKeyboardButton("Give Sensitivity 🎮", callback_data="give_sensi")
    )
    bot.reply_to(message,
        "🎮 *𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗙𝗥𝗘𝗘 𝗙𝗜𝗥𝗘 𝗦𝗘𝗡𝗦𝗜𝗧𝗜𝗩𝗜𝗧𝗬 𝗕𝗢𝗧* 🎉\n"
        "*𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗕𝗬:* @dg_gaming_1m 🚀\n"
        "𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 👇",
        parse_mode="Markdown",
        reply_markup=markup
    )

# ✅ /give command
@bot.message_handler(commands=['give'])
def give_command(message):
    bot.reply_to(message,
        "🎮 𝗣𝗟𝗘𝗔𝗦𝗘 𝗥𝗘𝗣𝗟𝗬 𝗧𝗢 𝗔 𝗨𝗦𝗘𝗥'𝗦 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗔𝗡𝗗 𝗦𝗘𝗟𝗘𝗖𝗧 𝗔𝗡𝗗𝗥𝗢𝗜𝗗 𝗢𝗥 𝗜𝗢𝗦 👇"
    )

# ✅ Sirf admin ke liye
@bot.message_handler(commands=['startsensi'])
def startsensi_command(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "❌ 𝗢𝗡𝗟𝗬 𝗕𝗢𝗧 𝗔𝗗𝗠𝗜𝗡 𝗖𝗔𝗡 𝗨𝗦𝗘 /startsensi")
        return
    bot.reply_to(message, "✅ 𝗔𝗗𝗠𝗜𝗡 𝗔𝗖𝗖𝗘𝗦𝗦 𝗚𝗥𝗔𝗡𝗧𝗘𝗗. 𝗦𝗘𝗡𝗦𝗜𝗧𝗜𝗩𝗜𝗧𝗬 𝗕𝗢𝗧 𝗦𝗧𝗔𝗥𝗧𝗘𝗗.")

# ✅ Callback button
@bot.callback_query_handler(func=lambda call: call.data == "give_sensi")
def handle_sensi_button(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "🎮 𝗨𝗦𝗘 /give 𝗧𝗢 𝗚𝗘𝗧 𝗬𝗢𝗨𝗥 𝗦𝗘𝗡𝗦𝗜𝗧𝗜𝗩𝗜𝗧𝗬 𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦.")

# ✅ Polling se bot chalu rakho
bot.polling()