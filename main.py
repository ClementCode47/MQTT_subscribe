import RPi.GPIO as GPIO
import dht11
import paho.mqtt.client as mqtt

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=11)
result = instance.read()

if result.is_valid():
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)
    import paho.mqtt.client as mqtt


broker = "10.4.1.42"
client = mqtt.Client("Johnny", clean_session=False)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("SMILE", qos=2)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

client.loop_forever()
