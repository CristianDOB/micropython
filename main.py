
# Importando a classe RedeW do módulo rede
from rede import RedeW
# Importando as bibliotecas necessárias
# utime: para usar o método sleep
import utime
# umqttsimple: para usar o protocolo MQTT
from umqttsimple import MQTTClient
# ubinascii: para usar o método hexlify
import ubinascii
# machine: para usar o método unique_id
import machine

# Instanciando a classe RedeW
wifi_connection  = RedeW()

utime.sleep(8)
if not wifi_connection.check_connection():
    wifi_connection.connect_using_credentials()
else:
    print('\n\n\n Already connected.\n\n\n')
    wifi_connection.show_connection_info()

mqtt_server = "broker.emqx.io"
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'teste'

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  utime.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  print(f"Ocorreu um erro: {e}")
  restart_and_reconnect()

client.publish(topic_pub, b'Hello World!')


