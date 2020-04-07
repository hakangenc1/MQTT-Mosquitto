
import paho.mqtt.publish as publish

while True:
    message = input("Please enter your message: ")
    publish.single("test/topic", message, hostname="test.mosquitto.org")
    print("Message sent!")