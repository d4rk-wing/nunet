from machine import Pin, SoftI2C
import time
from modulos import ssd1306 
from framebuf import FrameBuffer, MONO_HLSB

# ESP32 Pin assignment
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def imp_oled_1r(x):
    oled.text(x, 0, 32, 1)
    oled.show()
    time.sleep(3)
    oled.fill(0)
    
def imp_oled_2r(x,y):
    oled.text(x, 0, 16, 1)
    oled.text(y, 0, 32, 1)
    oled.show()
    time.sleep(3)
    oled.fill(0)
    
def imp_oled_3r(x,y,z):
    oled.fill(0)
    oled.text(x, 0, 8, 1)
    oled.text(y, 0, 23, 1)
    oled.text(z, 0, 40, 1)
    oled.show()
    time.sleep(3)
    oled.fill(0)
    
def mostrarLogoInicial():
    dibujo= open("images/nunet.pbm", "rb")  # Abrir en modo lectura de bist
    dibujo.readline() # metodo para ubicarse en la primera linea de los bist
    xy = dibujo.readline() # ubicarnos en la segunda linea
    x = int(xy.split()[0])  # split  devuelve una lista de los elementos de la variable solo 2 elemetos
    y = int(xy.split()[1])
    icono = bytearray(dibujo.read())  # guardar en matriz de bites
    dibujo.close()
    oled.blit(FrameBuffer(icono, x, y, MONO_HLSB), 0, 0) # ruta y sitio de ubicación
    oled.show()  #mostrar
    time.sleep(3)
    oled.fill(0)
    
def printOled(msg,metric):
    #oled.invert(lightMode)
    oled.fill(0)
    oled.text("#"*120,1,1)
    oled.text("{}".format(msg),0,15)
    oled.text("m3: {}".format(metric),0,30)
    oled.text("Still monitoring",0,50)
    oled.show()