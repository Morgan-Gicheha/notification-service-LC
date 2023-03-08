import pika, sys, os
# from classes import serviceSelector
from tools.rabbitMQ.classes import serviceSelector


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="notification")

    def callback(ch, method, properties, body):
        selectorInstance = serviceSelector.NotificationWorker(body)
        selectorInstance.rabbitMQCallback()

    channel.basic_consume(
        queue="notification", on_message_callback=callback, auto_ack=True
    )

    print(" [*] Notification Service Listening...")
    channel.start_consuming()
