import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
ADMIN_ID = "YOUR_ADMIN_ID_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Cari Judul V1", callback_data="cari_v1"),
         InlineKeyboardButton("Cari Judul V2", callback_data="cari_v2")],
        [InlineKeyboardButton("Beli VIP", callback_data="beli_vip"),
         InlineKeyboardButton("Profile", callback_data="profile")],
        [InlineKeyboardButton("Lapor Kendala", callback_data="lapor"),
         InlineKeyboardButton("Cari Cuan Referal", callback_data="referal")],
        [InlineKeyboardButton("Request Drama", callback_data="request"),
         InlineKeyboardButton("List Tutorial", callback_data="tutorial")],
        [InlineKeyboardButton("Pembayaran Malaysia/Manual", callback_data="pembayaran")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        text="🎬 *GROUP SHORTID_BOT PREMIUM*\n\nPilih menu di bawah:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    routes = {
        "cari_v1": "🔎 *Cari Judul V1*\n🌐 [Buka WebApp](https://shortid-premium-bot.onrender.com/v1)",
        "cari_v2": "🔎 *Cari Judul V2*\n🌐 [Buka WebApp](https://shortid-premium-bot.onrender.com/v2)",
        "beli_vip": "💎 *Beli VIP*\nHubungi admin untuk upgrade premium.",
        "profile": "👤 *Profile*\nMenampilkan data akun kamu.",
        "lapor": "⚠️ *Lapor Kendala*\nSilakan kirim pesan ke admin.",
        "referal": "💰 *Cari Cuan Referal*\nDapatkan bonus dari undangan teman!",
        "request": "📩 *Request Drama*\nTulis judul yang ingin kamu minta.",
        "tutorial": "🎓 *List Tutorial*\nBerisi panduan lengkap pengguna.",
        "pembayaran": "💳 *Pembayaran Malaysia / Manual*\nHubungi admin untuk konfirmasi pembayaran."
    }

    text = routes.get(query.data, "Menu tidak ditemukan.")
    await query.edit_message_text(text=text, parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("🤖 Bot sedang berjalan (Polling Mode)...")
    app.run_polling()

if __name__ == "__main__":
    main()

