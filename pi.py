import paho.mqtt.client as mqtt
#import Adafruit_SSD1306
#from PIL import Image, ImageDraw, ImageFont

#disp = Adafruit_SSD1306.SSD1306_128_32(rst=0)
#disp.begin()
#FONT_PATH = '/usr/share/fonts/truetype/piboto/PibotoCondensed-Regular.ttf'
#FONT = ImageFont.truetype(FONT_PATH, 22)
	# Callback fires when conected to MQTT broker.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code {0}'.format(rc))
    # Subscribe (or renew if reconnect).
    client.subscribe('temp_humidity')


# Callback fires when a published message is received.
def on_message(client, userdata, msg):
    t = [float(x) for x in msg.payload.decode("utf-8")]
    print(t)


client = mqtt.Client()
client.on_connect = on_connect  # Specify on_connect callback
client.on_message = on_message  # Specify on_message callback
client.connect('localhost', 1883, 60)  # Connect to MQTT broker (also running on Pi).

# Processes MQTT network traffic, callbacks and reconnections. (Blocking)
client.loop_forever()
