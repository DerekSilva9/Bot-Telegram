import telebot
from telebot import types

API_KEY = "Seu Token da API"

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["Comandos"])
def comandos(mensagem):
    texto = ('texto exibido ao executar o comando')

    markup = types.InlineKeyboardMarkup()
    botao = types.InlineKeyboardButton("Botão", url="https://seu_link.com")
    markup.add(botao)

    bot.reply_to(mensagem, texto, reply_markup=markup)

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = ('Texto exibido ao escrever qualquer mensagem')
    bot.reply_to(mensagem, texto)


bot.polling()