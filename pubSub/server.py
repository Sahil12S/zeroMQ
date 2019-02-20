# 
# Weather update server
# Bind PUB socket to tcp://*5556
# Publishes random weather updates
# 

import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    zipcode = randrange(1, 100000)
    temprature = randrange(-80, 135)
    relHumidity = randrange(10, 60)

    socket.send_string("%i %i %i" % (zipcode, temprature, relHumidity))