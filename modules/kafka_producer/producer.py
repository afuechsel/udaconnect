import json
import random
from kafka import KafkaProducer
from datetime import datetime

TOPIC_NAME = 'locations'
KAFKA_SERVER = 'localhost:9092'

# sample latitudes from the database
latitudes = ["-122.2905209999999983",
             "-122.2905240000000049",
             "-122.2908829999999938",
             "34.0585135999999977",
             "35.0585060000000013",
             "35.0585135999999977",
             "35.0585639999999970"]

# sample longitudes from the database
longitudes = ["-105.5719565999999929",
              "-106.5719521000000043",
              "-106.5719560999999942",
              "-106.5719565999999929",
              "-106.5721845000000059",
              "-106.5721845999999999",
              "-106.5722575000000063",
              "37.5534409999999994",
              "37.5534510000000026",
              "37.5536299999999983"]

# ids of the sample persons in the database
persons = [1, 5, 6, 8, 9]

def getRandomPersonId():
    # for demonstration purposes only - get a random person 
    return persons[random.randint(0, len(persons ) - 1)]


def getCurrentLatitude():
    # for demonstration purposes only - get a randomly picked latitude
    return latitudes[random.randint(0, len(latitudes) - 1)]


def getCurrentLongitude():
    # for demonstration purposes only - get a randomly picked longitude
    return longitudes[random.randint(0, len(longitudes) - 1)]


producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda m: json.dumps(m).encode('utf-8'))

location = dict({
    "person_id": getRandomPersonId(),
    "creation_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
    "latitude": getCurrentLatitude(),
    "longitude": getCurrentLongitude()
})


producer.send(TOPIC_NAME, location)
producer.flush()
