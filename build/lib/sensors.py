import publisher as Publisher
import time
import paho.mqtt.client as mqtt
import json
import _thread

def publisherStart():

    """ Create several temperature sensor objetcts and send them to brocker
    """

    numNodes = 3 # number of temperature sensors in the room
    interval = 1 # time (seconds) that each sensor send data
    objs = Publisher.generateNodes(numNodes) # generate temp objects array

    while True:

      for i in range(numNodes):
        data = Publisher.formatTemperature(i) # create json string
        objs[i].publish("/readings/temperature", json.dumps(data)) # publish data to mqtt

      time.sleep(interval)

    for client in objs:
        client.loop_stop();
        client.disconnect()



def main():

    """ Main function
    """

    try:

        print("Starting Publisher...")
        _thread.start_new_thread(publisherStart, () ) # create publisher thread




    except:
        print("Unable to start threads")

    while 1:
        pass


main()