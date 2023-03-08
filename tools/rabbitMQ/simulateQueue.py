import pika
import json

# available types -->> sms, email, telegram
dummyPayload = {
    "type": "telegram",
    "from": "littleApp",
    "message":"Hello world.",
    "to": [
        "Little_Alerts",
        "Little_Gicheha",
        "Little_Morgab",
        "Little_coder",
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