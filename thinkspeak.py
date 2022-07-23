from urllib import response
import urequests

def send_thinkspeak(Q,location):
    url = "https://api.thingspeak.com/update?api_key=FYGRZLYAIV64ELYD&field1=0"

    response = urequests.get(url+"&field1="+str(Q)+"&field1="+str(location))

    if response.status_code == 200:
        print("Item successfully updated")
        print("{}: {}".format(location, Q))
    else:
        print("Item failed to update. Response: {}".format(response.status_code))