# Micropython_RaspberryPi
Verified codes dumped on esp32 using R_Pi

Before uploading the firmware, please make sure the Pi is up-to-date.  From a terminal, type the following:
```
sudo apt-get update && sudo apt-get upgrade
```
A utility called ESPTool is used to upload the MicroPython firmware to the ESP32.  It is installed using pip3 to target Python3:
```
sudo pip3 install esptool
```
Next the USB port needs to be determined using :
```
pi@raspberrypi:~/Desktop/Ankita $ dmesg | grep ttyUSB
```
The results should show a CP210x UART to USB bridge attached to a USB port.  Below the port is ttyUSB0.
```
[ 3636.546701] usb 1-3: cp210x converter now attached to ttyUSB0
```
To burn the firmware
```
esptool.py --port /dev/ttyUSB0 write_flash 0x1000 esp32-20190306-v1.10-16
```
The ESPTool flash_id command can be used to ensure everything is working.The port name returned by the dmesg command above.

```
esptool.py --port /dev/ttyUSB0 write_flash 0x1000 esp32-20190306-v1.10-16
esptool.py --port /dev/ttyUSB0 flash_id
```
Expected outcome of the first command
```
esptool.py v2.0.1

Connecting........_

Detecting chip type... ESP32

Chip is ESP32D0WDQ6 (revision 0)

Uploading stub...

Running stub...

Stub running...

Manufacturer: c8

Device: 4016

Detected flash size: 4MB

Hard resetting...
```
Before uploading the firmware it is recommended to erase the ESP32, which can also be done with the ESPTool:
```
esptool.py --port /dev/ttyUSB0 erase_flash
```
A copy of the MicroPython firmware is required.  You could just download a ready-to-go daily build from :
http://micropython.org/download#esp32


Once the firmware is downloaded it can be uploaded with the ESPTool using the write_flash command.  The hex value indicates the starting memory address and it is followed by the path to the downloaded MicroPython ESP32 firmware file.

The starting address now needs to be 0x1000 instead of zero.
```
esptool.py --port /dev/ttyUSB0 write_flash 0x1000 <path to firmware file>
```
Ideally you want a program that provides a REPL terminal and also can perform file management.  We'll be using rshell.  It can be installed using pip:
```
sudo pip3 install rshell
```
This simple program will run on the Raspberry Pi and allow you to access the REPL terminal on the ESP32.  It also provides file management to transfer and manipulate files on both the Pi and the ESP32.  To start rshell, type rshell and specify 30 for the buffer size and your USB port:
```
pi@raspberrypi:~/Desktop/Ankita $ rshell --buffer-size=30 -p /dev/ttyUSB0
```
The first prompt can be used to execute file commands. We enter the shell through which we can dump files onto esp32The output looks like:  
```
Using buffer-size of 30

Connecting to /dev/ttyUSB0 (buffer-size 30)...

Testing if ubinascii.unhexlify exists ... Y

Retrieving root directories ... /boot.py/ /ConnectWifi.py/ /post_request.py/ /simple.py/ /mqtt.py/ /localhost.py/ /app.py/ /umqtt/ /www/ /hc2.png/ /CNAME/ /main.py/ /microWebSrv.py/ /microWebTemplate.py/ /LICENSE.md/ /microWebSocket.py/ /mosquitto-1.5.8/ /dht_web.py/ /dht.html/ /huewheel.min.js/ /start.py/ /led_web.py/ /led.html/

Setting time ... Mar 10, 2019 10:38:00

Evaluating board_name ... pyboard

Retrieving time epoch ... Jan 01, 2000

Welcome to rshell. Use Control-D (or the exit command) to exit rshell.

/home/pi/Desktop/Ankita> 
```
Type repl to open the MicroPython programing environment.  The terminal will now accept Python code.  For example, print hello world, outputs hello world.
```
/home/pi/Desktop/Ankita> repl
```
The output:
```
Entering REPL. Use Control-X to exit.
>
MicroPython v1.10-54-g43a894fb4 on 2019-02-07; ESP32 module with ESP32
Type "help()" for more information.
>>>

#We can try printing "Hello World"
>>> print('Hello World')
Hello World
```
Back in rshell type ctrl-X if you are still in the REPL to exit back to the main rshell terminal.  Navigate to the folder where the program is saved.  You can use cd and ls just like in a regular terminal.  Then use cp to copy the program file to the ESP32 which is specified with /pyboard:
```
/home/pi/Desktop/Ankita> cp ConnectWifi.py /pyboard
```

Type repl to return the REPL and type import ConnectWifi to run the ConnectWifi.py program.
```
Entering REPL. Use Control-X to exit.
>
MicroPython v1.10-168-g62483bb95 on 2019-03-05; ESP32 module with ESP32
Type "help()" for more information.
>>> 
>>> import ConnectWifi
```
output:
```
('192.168.0.127', '255.255.255.0', '192.168.0.1', '192.168.0.1')
```


Similarly running a http post request to the localhost server of Raspberry Pi
```
/home/pi/Desktop/Ankita> cp post_request.py /pyboard

/home/pi/Desktop/Ankita> repl
Entering REPL. Use Control-X to exit.
>
MicroPython v1.9.1-218-g56f05137 on 2017-07-01; ESP32 module with ESP32
Type "help()" for more information.
>>> 
>>> import post_request
```
Since this is a code to post http requests. The output looks as follows:

```
GET!!!!
{
  "message": "Hello!"
}
b'OK'
```
