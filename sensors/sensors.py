import publisher as Publisher
import time
import json
import _thread
import os


def publisherStart():
    """ Create temperature sensor objetct and send them to brocker
    """
    sensorID = os.getenv('SENSOR_ID')
    interval = 1  # time is in second
    obj = Publisher.generateSensor()  # generate temp object
    while True:
        data = Publisher.formatTemperature(sensorID)  # produce json string
        obj.publish("/readings/temperature", json.dumps(data))  # publish data to mqtt
        time.sleep(interval)
    client.loop_stop();
    client.disconnect()


def main():
    """ Main function
    """
    try:
        print("Starting Publisher ")
        _thread.start_new_thread(publisherStart, ())  # produce publisher thread

    except:
        print("Con not to start threads")
    while 1:
        pass


if __name__ == "__main__":
    main()
