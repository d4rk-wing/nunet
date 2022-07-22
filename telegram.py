from modulos.utelegram import Bot
from machine import Pin
led = Pin(2, Pin.OUT)

TOKEN = 'TOKEN_TELEGRAM'
bot = Bot(TOKEN)

@bot.add_command_handler('help')
def help(update):
    update.reply('Write on to power the led on \nWrite off to power the led off \nWrite /value to retrieve the current status of the led')

@bot.add_command_handler('value')
def value(update):
    if led.value():
        update.reply('LED is on')
    else:
        update.reply('LED is off')

@bot.add_message_handler('^on|On|ON$')
def on(update):
    led.on()
    update.reply('LED is on')
    
@bot.add_message_handler('^off|Off|OFF$')
def off(update):
    led.off()
    update.reply('LED is off')