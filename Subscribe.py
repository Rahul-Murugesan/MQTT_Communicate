import paho.mqtt.client as mqtt

# Define the MQTT broker details
mqtt_broker = "broker.mqtt-dashboard.com"
mqtt_port = 1883
mqtt_topic = "outTopic1"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(mqtt_topic)
    else:
        print("Connection failed with code", rc)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign event callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(mqtt_broker, mqtt_port, 60)

# Start the MQTT client
client.loop_forever()
