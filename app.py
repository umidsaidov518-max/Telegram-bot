import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define the bot token and create the Updater
TOKEN = 'YOUR_BOT_TOKEN_HERE'
updater = Updater(token=TOKEN, use_context=True)

# Define a command handler to start the bot
def start(update, context):
    update.message.reply_text('Hello! I am your Telegram bot.')

# Define a message handler for text messages
def echo(update, context):
    update.message.reply_text(update.message.text)

# Add handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the bot
updater.start_polling() 
updater.idle()