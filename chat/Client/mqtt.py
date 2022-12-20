import random
import time, threading

from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

class Mqtt():
    
    def __init__(self, client_id: int, usr: str, pwd: str, broker: str, port: int):
        self.client = self.connect_mqtt(client_id, usr, pwd, broker, port)
    
    def connect_mqtt(self,client_id: int, usr: str, pwd: str, broker: str, port: int) -> mqtt_client:
        client = mqtt_client.Client(client_id)
        client.username_pw_set(username, password)
        client.on_connect = self.on_connect
        client.connect(broker, port)
        return client
    
    def disconnect(self):
        self.client.disconnect()
    
    def on_connect(self,client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

    def subscribe(self, topic: str):
        self.client.subscribe(topic)
        #self.client.on_message = self.on_message
        
    def on_message(self, client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
    
    def publish(self,topic_msg: str, payload: str):
       
        result = self.client.publish(topic_msg, payload)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{payload}` to topic `{topic_msg}`")
            return True
        else:
            print(f"Failed to send message to topic {topic_msg}")
            return False
          
            
    def loop_forever(self):
        self.thread = threading.Thread(target = self.client.loop_forever, args=())
        self.thread.start()
        
def main():
    client = Mqtt(client_id, username, password, broker, port)
    
    client.subscribe("application/+/device/+/rx")
    client.loop_forever()
    
    while 1:
        msg ='''{\"confirmed\":false,\"data\":\"%s\",\"devEUI\":\"%s\",\"fCnt\":0,\"fPort\":2}''' % ("BQECQwg=","0080e1150508f01b")
        #client.publish(topic_downlink,msg)
        time.sleep(5)

if __name__ == '__main__':
    main()