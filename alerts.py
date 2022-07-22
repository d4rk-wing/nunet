from machine import Pin
import oled
import utime
import telegram

red = Pin(12, Pin.OUT)
green = Pin(13, Pin.OUT)
blue = Pin(14, Pin.OUT)

buzz = Pin(27, Pin.OUT)

def ok_for_now(V):
    #Alerta RGB
    red.value(0)
    green.value(204)
    blue.value(0)
    #Alerta Oled
    oled.imp_oled_3r("Consumo de agua ","aceptable"," "+V)
    utime.sleep(3)
    #Alerta Telegram

def so_close(V):
    #Alerta RGB
    red.value(255)
    green.value(255)
    blue.value(0)
    #Alerta Oled
    oled.imp_oled_3r("Consumo de agua","cerca del limite:","  " + V)
    utime.sleep(3)
    #Alerta Telegram

def far_away(V):
    #Alerta RGB y Buzz
    red.value(255)
    green.value(0)
    blue.value(0)
    buzz.value(True)
    #Alerta Oled
    oled.imp_oled_3r("Consumo de agua","supero el limite","  "+V)
    utime.sleep(3)
    #OFF
    buzz.value(False)
    #Alerta Telegram
    
def off():
    #OFF
    red.value(0)
    green.value(0)
    blue.value(0)
    buzz.value(False)
    #Alerta Telegram
    
def printOled(msg,metric):
    oled.fill(0)
    oledtext("#"*120,1,1)
    oled.text("{}".format(msg),0,15)
    oled.text("m3: {}".format(metric),0,30)
    oled.text("Still monitoring",0,50)
    oled.show()