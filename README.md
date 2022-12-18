# ChatGPT Telegram Bot

This is a simple Telegram bot that uses OpenAI's GPT-3 (Generative Pre-trained Transformer 3) language model to generate responses to user messages.

## Requirements

To run this bot, you will need the following Python packages:
- `openai`
- `telegram`

You will also need a Telegram bot token and an OpenAI API key.

## Configuration

To configure the bot, edit the following lines in the code:
- Set the value of `openai.api_key` to your OpenAI API key.
- Set the value of `bot = telegram.Bot(token='<YOUR TOKEN HERE>')` to your Telegram bot token.

## Usage

To start the bot, run the `main.py` script. The bot will listen for messages in any chats that it is a member of and generate a response using GPT-3.

## Customization

You can customize the behavior of the bot by modifying the following parameters in the `generate_response()` function:
- `engine`: The name of the GPT-3 instance to use.
- `prompt`: The prompt to provide to GPT-3.
- `max_tokens`: The maximum number of tokens (i.e. words or punctuation marks) to generate in the response.
- `temperature`: A value that controls the randomness of the generated response. A higher temperature will generate more varied responses, while a lower temperature will generate more predictable responses.

You can also customize the start command handler function, `start()`, to specify a different message to send when the `/start` command is received.
