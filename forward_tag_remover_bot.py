from telethon import TelegramClient, events

# Replace these with your own values
api_id = '27601650'
api_hash = '57ba09bc57e6df472fcf9fbafc01fbe7'
bot_token = '7308141752:AAG4BKBoh35JR96VFma2uy1laqeDuD0viUY'

# Initialize the Telegram client
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handle_message(event):
    if event.message.forward:  # Check if the message is forwarded
        if event.message.media:
            # Forward large files, including ZIPs
            await client.send_file(
                event.chat_id, 
                event.message.media, 
                caption=event.message.text if event.message.text else None
            )
        else:
            # Forward text messages
            await client.send_message(event.chat_id, event.message.text)
    else:
        await event.reply("This message is not forwarded or does not contain media.")

print("Bot is running...")
client.run_until_disconnected()
