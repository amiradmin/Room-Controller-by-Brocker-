import random
import time
import paho.mqtt.client as mqtt
import json
import numpy


## genTemperature: generates uniform data with a specified interval :##


minRange = 20.0 # min temp range for temp. simulation
maxRange = 27.0 # max temp range for temp. simulation
tempInterval = 0.5 # interval for genTempCase = 0 (uniform temp array)

indexCounter = 0

#create a uniform array for genTempCase = 0
tempCase1 = numpy.arange(minRange, maxRange, tempInterval).tolist()

def genTemperature(minRange,maxRange):

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

  data['value'] = genTemperature(minRange, maxRange)

  return data


def generateNodes(numNodes):

  """ Generate temperature sensor objects
  """

  objs = [mqtt.Client() for i in range(numNodes)]

  for i in range(numNodes):
    objs[i].connect("localhost", 1883, 60)
    objs[i].loop_start()

  return objs