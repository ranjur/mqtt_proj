# Project Setup

## Set up Virtual Environment

1. Create a virtual environment:
    ```bash
    python3.12 -m venv virtual
    ```

2. Activate the virtual environment:
    ```bash
    source ../virtual_new/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django server:
    ```bash
    python manage.py runserver
    ```

## Trigger MQTT Message Manually

1. Install Mosquitto and Mosquitto clients:
    ```bash
    sudo apt-get install mosquitto mosquitto-clients
    ```

2. Start the Mosquitto service:
    ```bash
    sudo systemctl start mosquitto
    ```

3. Enable Mosquitto to start on boot:
    ```bash
    sudo systemctl enable mosquitto
    ```

4. Send MQTT messages with the following command:
    ```bash
    mosquitto_pub -h localhost -t "test/topic" -m "Hello, MQTT from Django!"
    ```

## Testing the WebSocket

1. Use Django Channels with Daphne to test the WebSocket setup.

## Testing the MQTT Functionality

1. Open `mqtt_check.html` in your browser to check the MQTT setup.