import logging
from telethon import TelegramClient, events
from telethon.tl.functions.channels import EditBanned
from telethon.tl.types import ChatBannedRights

# 🛠️ Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🏆 Telegram API credentials
API_ID = '29755489'
API_HASH = '05e0d957751c827aa03494f503ab54fe'
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# 🚀 Initialize Client
client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# 🏷️ Channel ID (Negative ID for channels)
CHANNEL_ID = -1001234567890  

# 🔒 Ban Rights (Permanent Ban)
BAN_RIGHTS = ChatBannedRights(
    until_date=None,     # None = Permanent ban
    view_messages=True   # Prevent user from viewing messages
)

@client.on(events.ChatAction)
async def handle_user_leave(event):
    try:
        if event.user_left or event.user_kicked:
            user_id = event.user_id
            logger.info(f"User {user_id} left or was kicked. Attempting to ban...")

            # ✅ Ban the user
            await client(EditBanned(CHANNEL_ID, user_id, BAN_RIGHTS))
            logger.info(f"✅ User {user_id} banned successfully.")

    except Exception as e:
        logger.error(f"❌ Error while banning user {event.user_id}: {e}")

def main():
    logger.info("🚀 Bot is now running...")
    client.run_until_disconnected()

if __name__ == "__main__":
    main()