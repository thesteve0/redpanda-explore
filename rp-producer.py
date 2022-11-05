from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', batch_size=1, client_id="Steve's code")

for x in range(10):
    index = 'batch_size=0: ' + str(x)
    producer.send('foobar', index.encode('utf-8'))
# producer.flush()
print("done")