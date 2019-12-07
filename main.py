from time import sleep
import paho.mqtt.client as mqtt


CLIENT_ID = "P1"
BROKER    = ""  # Broker ip or hostname
TOPIC     = ""  # Mqtt topic used by the smart outlet

# Main program:
if __name__ == "__main__":
  client = mqtt.Client(CLIENT_ID)
  client.connect(BROKER)
  client.loop_start()

  print("Starting pairing process")
  print("Lamp On")
  client.publish(TOPIC, '{"state":"ON"}')
  sleep(2)
  print(" ")

  for i in range(0, 6):
    print("Lamp Off")
    client.publish(TOPIC, '{"state":"OFF"}')
    sleep(1)
    print("Lamp On")
    client.publish(TOPIC, '{"state":"ON"}')
    sleep(500 / 1000)

  sleep(2)
