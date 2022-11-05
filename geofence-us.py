from kafka import KafkaConsumer
import json

## this app consumes the coords topic and checks if the coords are in the United States

lat_max = 49.384358
lat_min = 24.396308
lon_max = -66.885444
lon_min = -124.848974

def check_fence(id, lat, lon):
    if lat < lat_max and lat > lat_min:
        if lon < lon_max and lon > lon_min:
            print("WE ARE IN THE U.S. with id " + id)


if __name__ == '__main__':

    print("look for events in USA")
    consumer = KafkaConsumer(
        'coords',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='the_best_group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    for message in consumer:
        message = message.value
        check_fence(id = message["id"], lat = message["lat"], lon=message["lon"])
