import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import openai

openai.api_key = "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"

async def gpt_response(prompt):
  response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  temperature=0.9,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
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
    application = ApplicationBuilder().token('5732485928:AAHSXwkZpMXD_Hu2fuHvsZd5R2jiIAUnVu4').build()
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    application.run_polling()