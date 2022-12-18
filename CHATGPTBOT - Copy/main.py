import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Set the OpenAI API key
openai.api_key = "X"

# Create the Telegram bot and get the updater
bot = telegram.Bot(token='X')
updater = Updater(bot=bot, use_context=True)

# Define the start command handler
def start(update: Updater, context: CallbackContext):
    update.message.reply_text('Hello, welcome to the chatbot!')

# Define the function to generate a response from GPT-3
def generate_response(prompt):
    """Generate a response from GPT-3 based on the given prompt."""
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.6,
    )

    message = completions.choices[0].text
    return message

# Define the message handler function
def handle_message(update, context: CallbackContext):
    """Handle incoming messages and generate a response using GPT-3."""
    # Get the message text and sender information
    message_text = update.message.text
    sender = update.message.from_user
    
    # Generate a response from GPT-3
    response = generate_response(prompt=message_text)
    
    # Send the response to the chat
    context.bot.send_message(chat_id=update.message.chat_id, text=response)

# Set up the command and message handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Set up the error handler
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

updater.dispatcher.add_error_handler(error_callback)

# Start the updater
updater.start_polling()
