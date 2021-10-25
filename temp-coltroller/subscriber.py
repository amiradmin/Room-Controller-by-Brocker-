import json


tempArr = [None] * 3  # array that used for saving multiple sensor averages
average = ""
setPoint = 22  # Favorite temperature
temperatureControlArr = [1]  # variable for samples of saving multiple temperature
sampingInterval = 3  # default interval factor before activating valve


# the callback when the client got a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we miss the connection and
    # reconnect so that subscriptions will be renewed.
    client.subscribe("/readings/temperature")


# The callback for when the client receives a PUBLISH message from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))
    calcAverage(client, msg.payload)


def calcAverage(client, message):
    """ Parse temperature JSON and calculate average for overall room temperature
    """
    if not any(v is None for v in tempArr):  # if we have collected all data from sensors in the room
        average = sum(tempArr) / len(tempArr)  # calculate average temperature of room
        temperatureControl(client, average)  # apply control to valve
        for i in range(0, len(tempArr)):
            tempArr[i] = None  # empty temp array

    data = json.loads(message)
    sensorNumber = data["sensorID"].split("-")
    tempArr[int(sensorNumber[1]) - 1] = int(data["value"])  # fill array depend on sensor id that received


def temperatureControl(client, currentTemp):
    """ simple fuzzy logic with 4 ranges
    (valve 100%) minThreshold <----- +- 2 | setPoint (50%) +- 2 | -----> maxThreshold (valve 0%)
    """

    global sampingInterval
    global setPoint
    data = {}
    maxThreshold = setPoint + 5  # maximum temperature threshold
    minThreshold = setPoint - 5  # minimum temperature threshold
    maxMidRangeTh = setPoint + 1  # middle maximum temperature threshold
    minMidRangeTh = setPoint - 1  # middle minimum temperature threshold

    # save all temperatures up to the samplingInterval
    # Example: if temperature sensor interval = 10 seconds and sampling interval = 10..
    #  Actuator will change interval * sampling interval = 100 seconds
    if (len(temperatureControlArr) != sampingInterval):
        temperatureControlArr.append(currentTemp)

    else:
        currentTemp = sum(temperatureControlArr) / len(temperatureControlArr)
        print("=" * 63)
        print("Average Temperature:{} ".format(currentTemp))
        del temperatureControlArr[:]

        if (currentTemp >= maxThreshold):  # tempe is above threshold, close the valve 0%. (fast movement)
            data['setLevel'] = 0
        elif (currentTemp <= minThreshold):  # temp is below threshold, close the valve 100%. (fast movement)
            data['setLevel'] = 100
        elif (currentTemp >= minMidRangeTh and currentTemp <= maxMidRangeTh):  # temp is close to set point
            data['setLevel'] = 0  # keep valve close for x time specified by sampling Interval.
            sampingInterval = 10  # make actuator to rest more time
        else:
            response = int(round((currentTemp * 50) / setPoint))  # get a percentage of openness
            sampingInterval = 5
            data['setLevel'] = response

        dumpData= json.dumps(data) # Create json message
        resp = json.loads(dumpData) #Testing  message and retriving set Level for Radiator
        print("Radiator Level: " + str(resp['setLevel']))
        print("="*63)


        client.publish("/radiator/room-1", json.dumps(data))  # publish data to mqtt
