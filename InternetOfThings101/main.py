#!/usr/bin/python

import paho.mqtt.client as paho
import psutil
import signal
import sys
import time

from threading import Thread

def interruptHandler(signal, frame):
    sys.exit(0)

def on_publish(mosq, obj, msg):
    pass

def dataNetwork():
    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

def dataNetworkHandler():
    idDevice = "90:b6:86:05:e7:d1"
    mqttclient = paho.Client()
    mqttclient.on_publish = on_publish
    mqttclient.connect("test.mosquitto.org", 1883, 60)
    while True:
        packets = dataNetwork()
        message = idDevice + " " + str(packets)
        print "MQTT dataNetworkHandler " + message
        mqttclient.publish("IoT101/Network", message)
        time.sleep(1)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, interruptHandler)

    threadx = Thread(target=dataNetworkHandler)
    threadx.start()

    while True:
        print "Richo Hello Internet of Things 101"
        time.sleep(5)

# End of File
