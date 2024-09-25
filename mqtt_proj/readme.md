Setup project
python3.12 -m venv virtual
source ../virtual_new/bin/activate
pip install -r requirements.txt
python manage.py runserver

To trigger MQTT message manually
sudo apt-get install mosquitto mosquitto-clients
sudo systemctl start mosquitto
sudo systemctl enable mosquitto

And run below command for sending messages
mosquitto_pub -h localhost -t "test/topic" -m "Hello, MQTT from Django!"

To test the websocket
use django channels with daphne


Open  mqtt_check.html in browser