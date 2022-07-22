import utime
from machine import Pin
from modulos import ufirebase as firebase

def send_fb (Q,location):
    fecha = utime.gmtime()
    key = "\""+location+"/"+str(fecha)+"\""
    print("Setting firebase")
    firebase.setURL("https://starry-seat-279623-default-rtdb.firebaseio.com/")
    print("Pushing data to DB")
    firebase.put(key,Q)
    print("Item successfully uploaded")
    print(key,Q)