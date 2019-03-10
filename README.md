# Micropython_RaspberryPi
Verified codes dumped on esp32 using R_Pi

#Before uploading the firmware, please make sure the Pi is up-to-date.  From a terminal, type the following:

sudo apt-get update && sudo apt-get upgrade

#A utility called ESPTool is used to upload the MicroPython firmware to the ESP32.  It is installed using pip3 to target Python3:

sudo pip3 install esptool

#Next the USB port needs to be determined using :

dmesg | grep ttyUSB

#The results should show a CP210x UART to USB bridge attached to a USB port.  Below the port is ttyUSB0.

[ 3636.546701] usb 1-3: cp210x converter now attached to ttyUSB0

#The ESPTool flash_id command can be used to ensure everything is working.The port name returned by the dmesg command above.

esptool.py --port /dev/ttyUSB0 flash_id

#Expected outcome of the first command

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

#Before uploading the firmware it is recommended to erase the ESP32, which can also be done with the ESPTool:

esptool.py --port /dev/ttyUSB0 erase_flash

#A copy of the MicroPython firmware is required.  You could just download a ready-to-go daily build from :
http://micropython.org/download#esp32


#Once the firmware is downloaded it can be uploaded with the ESPTool using the write_flash command.  The hex value indicates the starting memory address and it is followed by the path to the downloaded MicroPython ESP32 firmware file.

#The starting address now needs to be 0x1000 instead of zero.

esptool.py --port /dev/ttyUSB0 write_flash 0x1000 <path to firmware file>

#Ideally you want a program that provides a REPL terminal and also can perform file management.  We'll be using rshell.  It can be installed using pip:

sudo pip3 install rshell

#This simple program will run on the Raspberry Pi and allow you to access the REPL terminal on the ESP32.  It also provides file management to transfer and manipulate files on both the Pi and the ESP32.  To start rshell, type rshell and specify 30 for the buffer size and your USB port:

/home/ankita/Documents/micropython>rshell --buffer-size=30 -p /dev/ttyUSB0 

#The first prompt can be used to execute file commands. We enter the shell through which we can dump files onto esp32The output looks like:  #The boot.py file is automatically run at startup and contains low level code to set up the board and finish booting.  You typically don’t want to edit it.  However, you can add a file called main.py if you need your own code to run at start up after the boot.py.

#Type repl to open the MicroPython programing environment.  The terminal will now accept Python code.  For example, print hello world, outputs hello world.

/home/ankita/Documents/micropython>repl

#The output:

Entering REPL. Use Control-X to exit.
>
MicroPython v1.10-54-g43a894fb4 on 2019-02-07; ESP32 module with ESP32
Type "help()" for more information.
>>>

#We can try printing "Hello World"
>>> print('Hello World')
Hello World

#Back in rshell type ctrl-X if you are still in the REPL to exit back to the main rshell terminal.  Navigate to the folder where the program is saved.  You can use cd and ls just like in a regular terminal.  Then use cp to copy the program file to the ESP32 which is specified with /pyboard:

/home/ankita/Documents/micropython> cp post_request.py /pyboard

#Type repl to return the REPL and type import rgb to run the rgb.py program.

/home/ankita/Documents/micropython> repl
Entering REPL. Use Control-X to exit.
>
MicroPython v1.9.1-218-g56f05137 on 2017-07-01; ESP32 module with ESP32
Type "help()" for more information.
>>> 
>>> import post_request

#Since this is a code to post http requests. The output looks as follows:

POST!!!
201
b'Created'
{
  "id": 101
}
{'id': 101}
GET!!!!
{
  "userId": 1,
  "id": 1,
  "title": "quidem molestiae enim"
}
{'id': 1, 'userId': 1, 'title': 'quidem molestiae enim'}
200
b'OK'




