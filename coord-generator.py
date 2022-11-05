import json
import random
import string
import time


from kafka import KafkaProducer

# This program will generate random coordinatates somewhere on the globe
# and then send them to Kafka
def serializer(message):
    return json.dumps(message).encode('utf-8')

if __name__ == '__main__':
    startTime = time.time()

    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', value_serializer=serializer)
    print("Making coords")
    for x in range(10000):
        lat = random.uniform(-180.0, 180)
        lon = random.uniform(-180.0, 180)
        id = random.choice(string.ascii_uppercase)
        event = dict({"id": id, "lat": lat, "lon": lon})
        producer.send("coords", event)
        time.sleep(0.05)
    producer.flush()
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
    print("done")

