import publisher as Publisher
import time
import paho.mqtt.client as mqtt
import json
import _thread
import os

def publisherStart():

    """ Create temperature sensor objetct and send them to brocker
    """

    sensorID = os.getenv('SENSOR_ID')
    interval = 1 # time (seconds) that each sensor send data
    obj = Publisher.generateNodes() # generate temp object

    while True:


        data = Publisher.formatTemperature(sensorID) # create json string
        obj.publish("/readings/temperature", json.dumps(data)) # publish data to mqtt

        time.sleep(interval)


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


if __name__ == "__main__":
    main()