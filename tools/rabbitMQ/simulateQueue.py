import pika
import json

# available types -->> sms, email, telegram
dummyPayload = {
    "type": "sms",
    "from": "xoxo",
    "to": [
        "25479886xxxx",
    ],
}


def publish(data):

    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        channel = connection.channel()
    except Exception as error:
        print(" [x] RABBIT IS NOT RUNNING")
        return

    channel.queue_declare(queue="notification")
    channel.basic_publish(exchange="", routing_key="notification", body=json.dumps(data))
    print(" [x] Task published")
    connection.close()

publish(dummyPayload)