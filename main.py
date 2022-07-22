import _thread
from machine import enable_irq, disable_irq, Timer
from utime import sleep, ticks_ms, ticks_diff
import wifi
import oled
import caudalimetro

#Imprimir logo
oled.mostrarLogoInicial()

#Conectar Wifi

def red():
    if wifi.conectaWifi (wifi.ssid, wifi.passwd):
    
        print ("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', wifi.miRed.ifconfig())
        oled.imp_oled_2r("Conectado a",wifi.ssid)
    
    else:
        print ("Imposible conectar")
        oled.imp_oled_2r("Sin conexion","a red")
        miRed.active (False)

def do_main():
    red()
    #Iniciar caudalimetro
    caudalimetro.checkC()

if __name__ == "__main__":
    do_main()