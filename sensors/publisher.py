import random
import paho.mqtt.client as mqtt
import numpy
import os
## generateTemp: It produces uniform data with a determind interval :##

brokerID = os.getenv('BROKER_IP')
minRange = 20.0  # min temp range for temp simulation
maxRange = 27.0  # max temp range for temp simulation
tempInterval = 0.5  # interval for generateTemp (uniform temp array)

# Produce a uniform array for genTempCase
tempCase1 = numpy.arange(minRange, maxRange, tempInterval).tolist()


def generateTemp(minRange, maxRange):
    """ Returns a random temperature value within the given ranges
    """
    temp = random.randint(minRange, maxRange)
    return temp


def formatTemperature(sensorId):
    """ Generates JSON string for sending to MQTT
    """

    data = {}
    data['sensorID'] = 'sensor-' + str(sensorId)
    data['type'] = 'temperature'
    data['value'] = generateTemp(minRange, maxRange)

    return data


def generateSensor():
    """ Generate temperature sensor object
    """
    obj = mqtt.Client()
    obj.connect(brokerID, 1883, 60)
    obj.loop_start()

    return obj
