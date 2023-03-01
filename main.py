import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import openai
from dotenv import load_dotenv
import os

load_dotenv('key.env')
openai.api_key = os.getenv('OPENAPI_KEY')
token = os.environ.get('TOKEN')

async def gpt_response(prompt):
  response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  temperature=0.5,
  max_tokens = 256, 
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,

)
  return response['choices'][0]['text']


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = await gpt_response(update.message.text)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    application.run_polling()