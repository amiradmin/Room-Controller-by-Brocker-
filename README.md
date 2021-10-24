
## Multi-Sensor Room Temperature Controller 

This project is about an imaginary room with some sensors and
A radiator with electronic valve to keep the room's temperature 
on 22C as desire temp.<br />
the project has been dockerized for simplicity of implementation.<br />
####The project has decided into two parts
* Controller(Which its role is to received messaged and calculates average of temperature and control the radiator)
* Sensors(Which get the temperature from a sensor and create and sends a message to the brocker)
<br/>
Each part has its own topic in the broker:
* radiator/room-1 for controller
* readings/temperature for sensors
####List of containers:
* Mosquito 
* Controller
* Sensor 1
* Sensor 2
* Sensor 3
<br />
You can add more sensors by editing docker-compose file.<br />


####Installation:
1. Check and update docker-compose file according to your need and number of sensors you want 
2. Build and run containers with the help of docker compose
>docker-compose up -d
3. Run following command to execute a Mosquito container
>docker run -it -p 172.17.0.1:1883:1883 --name=mosquitto  toke/mosquitto
4. Run the following command to execute a controller container 
>docker exec -it controller python3 controller.py
5. Run the following command to execute a sensor(You should modify the sensor container name for more sensors)
> docker exec -it sensor1 python3 sensors.py
6. Run the following command to execute a sensor container command
>docker exec -it sensor2 python3 sensors.py
7. Run the following command to execute a sensor container command
>docker exec -it sensor3 python3 sensors.py

####Used technologies:
* Mosquito(It's light and suitable in comparison with other brokers like Rabbitmq and Kafka and also
possible to use it in some devices like Raspberry Pi and Arduino)
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



