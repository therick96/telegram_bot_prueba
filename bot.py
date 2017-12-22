import telebot # Importacion de libreria

# En telegram: @BotFather

TOKEN = '409659167:AAFxBcmYc1Jn2OyMMNzFiy-TL9eAmCZr93s' #Generado por BotFather

bot = telebot.TeleBot(TOKEN) # Creada instancia

print bot.get_me() #Obtener datos del bot