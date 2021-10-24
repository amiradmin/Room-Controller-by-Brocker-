import subscriber as Subscriber
import paho.mqtt.client as mqtt
import _thread


def subscriberInit():
    """ Initialize MQTT subscriber
    """

    client = mqtt.Client()
    client.on_connect = Subscriber.on_connect
    client.on_message = Subscriber.on_message
    client.connect("172.17.0.1", 1883, 60)
    client.loop_forever()


def main():
    """ Main function
    """
    try:
        print("Starting Subscriber...")
        _thread.start_new_thread(subscriberInit, ())  # create subscriber thread

    except:
        print("Unable to start threads")

    while 1:
        pass


if __name__ == "__main__":
    main()
