class NotificationWorker:
    """
    This class will hold the rabbitMQ callback function.
    """
    print("class has been called")
    def __init__(self, data) -> None:
        self.data = data

    def rabbitMQCallback(self):
        print(" [x] Received in class %r" % self.data)


# NotificationWorker({"name": "morgan"}).rabbitMQCallback()
