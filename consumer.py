import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()
ch.queue_declare("q1")

def demo(ch, method, prp, body):
    print(body)

ch.basic_consume(queue="q1", on_message_callback=demo, auto_ack=True)
ch.start_consuming()