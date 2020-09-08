#!/usr/bin/env python
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

parameters = pika.URLParameters('amqp://guest:guest@10.98.237.36:5672/%2f')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.basic_consume(
                        queue='monitoring-queue',
                        on_message_callback=callback,                      
                        auto_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()