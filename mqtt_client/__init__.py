import paho.mqtt.client as mqtt

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


# Callback when the client receives a response from the server
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribing to a topic
    client.subscribe("test/topic")

# Callback when a message is received from the server
def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} {msg.payload.decode()}")
    # async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
    send_message_view(f"Message received: {msg.topic} {msg.payload.decode()}")


# MQTT Client initialization
def mqtt_connect():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)  # Assuming Mosquitto is running locally

    client.loop_start()  # Start loop to listen for messages

mqtt_connect()


def send_message_view(message):
    # Get the channel layer
    channel_layer = get_channel_layer()

    # Define the group name (should match what your consumer uses)
    group_name = 'chat_group'

    # Send the message to the group
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'chat_message',  # This should match the handler method in the consumer
            'message': message,
        }
    )