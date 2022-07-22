from machine import Pin, Timer
import alerts
import oled
import utime
import firebase

# Initializing water sensor
s = Pin(25, Pin.IN)
clock = Timer(0)

# location and consumption limits settings
location="Bathroom"
limit_m3=8


pn = 0 # number of pulses
Q=0 # liters per minute

def count(pin):
    global pn
    pn += 1
    
def freq(timer):
    global pn, Q
    freq = pn
    Q = freq / 7.5
    #print(f"f= {freq} - Q = {Q}")
    pn = 0
    
def checkC():
    acumulado = 0
    ciclos = 0
    while True:

        oled.printOled(location, Q)
        s.irq(trigger = Pin.IRQ_RISING, handler = count )
        clock.init(mode = Timer.PERIODIC, period=1000, callback = freq )
        
        acumulado = acumulado + Q
        if acumulado == 0:
            alerts.off()
        if (acumulado <= limit_m3*0.7) and (acumulado != 0):
            alerts.ok_for_now(str(acumulado))
        if acumulado > limit_m3*0.7 and Q != 0 :
            alerts.so_close(str(acumulado))
        if acumulado >= limit_m3 and Q != 0:
            alerts.far_away(str(acumulado))
        utime.sleep(1)
        
        if Q == 0:
            ciclos +=1
        else:
            ciclos = 0
        print(str(acumulado)+" - "+str(ciclos))

        if ciclos >= 5 and acumulado != 0:
            firebase.send_fb(acumulado,location)
            acumulado = 0
            ciclos = 0
    