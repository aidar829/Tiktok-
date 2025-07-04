import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Токен возьмётся из настроек Render

async def start(update: Update, context):
    await update.message.reply_text("🔊 Отправьте ссылку на видео TikTok")

async def handle_tiktok(update: Update, context):
    url = update.message.text
    if "tiktok.com" not in url:
        await update.message.reply_text("❌ Это не ссылка TikTok!")
        return
    
    try:
        # Пример обработки (замените на реальный API TikTok)
        video_url = "https://example.com/video.mp4"  # Здесь будет ссылка на видео без водяного знака
        await update.message.reply_video(video=video_url)
    except Exception as e:
        await update.message.reply_text(f"⚠️ Ошибка: {str(e)}")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_tiktok))
    app.run_polling()
