
import network

ssid = "XxX"
password =  "jain12ankita"

station = network.WLAN(network.STA_IF)

#if station.isconnected() == True:
  #print("Already connected")
  #exit()

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print("Connection successful")
print(station.ifconfig())
