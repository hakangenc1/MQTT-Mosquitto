import paho.mqtt.client as mqtt

def on_connect(client, userData, flags, rc):
    print("Connected. Code: " + str(rc))

    client.subscribe("test/topic")
def on_message(client, userData, msg):
    print(msg.topic + ": " + str(msg.payload))




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()