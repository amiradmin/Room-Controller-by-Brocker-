
## Multi-Sensor Room Temperature Controller 

This project is about an imaginary room with some sensors and
A rediator with electronic valve to keep the room's temperature 
on 22C as desier temp.<br />
the project has been dockerized for simplicity of implementation.<br />
####The project has devided into two parts
* Controller(Which its role is to recieved messaged and calculates average of temperature and control the radiator)
* Sensors(Which get the temperature from a sensor and create ans sends a message to the brocker)

####List of contianers:
* Mossqitto 
* Controller
* Sensor 1
* Sensor 2
* Sensor 3
<br />
You can add more sensors by editing docker-compose file.<br />


####Installation:
1. 
2. Run following command to execute a Mossqitto container
>    docker run -it -p 1883:1883 --name=mosquitto  toke/mosquitto
2. Run the following command to execute a controller container 
>docker exec -it controller python3 controller.py
3. Run the following command to execute a sensor(You should modify the sensor container name for more sensors)
> docker exec -it sensor1 python3 sensors.py
4. Run the following command to execute a sensor container command
>docker exec -it sensor2 python3 sensors.py
5. Run the following command to execute a sensor container command
>docker exec -it sensor3 python3 sensors.py

####Used techmologies:
* Mosqitto(It's light and suitable in comperision with other brokers like Rabbitmq and Kafka and also
posibble to use it in some devices like Rasberry Pi and Arduino)
* Python 
* Threads for multi-threading process and speed up the code
* Numpy library to create a uniform array for get temperature
* Json for creating sensor's messages(for serializing and transmitting structured data over a network)<br />
<br />
I case of enough time I would use Queue for threading and MQTT Monitor for message queue monitoring
and also create on class include everything like controllers and sensors.


####Next Stage
Write a peace of code to create auto-detect sensors in a topic
and create codes for Arduino device to control and send real temperature
sensors like DHT11/DHT22 modules and also the same for controllers and electronic valves.



