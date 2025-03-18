import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.queue_declare(queue="q1")
ch.basic_publish(exchange='', routing_key='q1', body="HELLO MESSAGE")
connection.close()