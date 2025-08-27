import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# تأكد من أن هذه المكتبات مثبتة
# pip install telethon
# pip install pyrogram

# المتغيرات البيئية
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session_string = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")

eighthon = None

# التحقق من نوع الجلسة وتحويلها
if session_string:
    try:
        # المحاولة الأولى: التعامل معها كجلسة Telethon
        eighthon = TelegramClient(StringSession(session_string), API_ID, API_HASH)
        print("Using Telethon session string.")
    except ValueError:
        try:
            # المحاولة الثانية: إذا فشلت، جرب تحويلها من Pyrogram
            from pyrogram.types import Session
            
            # تحويل جلسة Pyrogram إلى تنسيق Telethon
            session_obj = Session(session_string)
            eighthon = TelegramClient(StringSession(session_obj.to_telethon()), API_ID, API_HASH)
            print("Using Pyrogram session string.")
        except Exception as e:
            print(f"Error: Invalid session string. Please provide a valid Telethon or Pyrogram session. {e}")
else:
    print("Error: No TERMUX session string found.")

# قم بتشغيل عميل المستخدم إذا كان صالحًا
if eighthon:
    eighthon.start()
    
# قم بتشغيل البوت
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=token)

ispay = ['yes']
ispay2 = ['yes']
