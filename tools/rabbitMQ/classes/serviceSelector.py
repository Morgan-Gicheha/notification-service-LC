import json

from utillities.sms import sms
# from utillities.email import email
from utillities.telegram import telegram

class NotificationWorker:
    """
    This class will hold the rabbitMQ callback function.
    """

    def __init__(self, data) -> None:
        self.data = json.loads(data)
        self.selectedService = None
        self.serviceType = None

    def rabbitMQCallback(self):
        print(" [x] Task Recived%r" % self.data)
        self.validateData(rawPayload=self.data)

    def validateData(self, rawPayload: dict):
        # if (not "type" in rawPayload or len(rawPayload["type"]) == 0) or (
        #     not "message" in rawPayload or len(rawPayload["message"]) < 9
        # ):
        #     print(
        #         "[x]- Invalid type provided, rejected or message length is less than 9"
        #     )
        #     return
        self.serviceCaller(cleanPayload=rawPayload)

    def serviceCaller(self, cleanPayload: dict):
        # telegram, sms, email

        #cleanPayload= {'type': 'te;legram', 'from': 'xoxo', 'to': ['25479886xxxx']}

        self.serviceType = cleanPayload["type"].lower()

        if self.serviceType == "sms".lower():
            print("-----------------")
            print(cleanPayload)
            print("-----------------")
            sms(cleanPayload["to"],cleanPayload["message"])
        elif self.serviceType == "telegram".lower():
            telegram(cleanPayload["message"],cleanPayload["to"])
        elif self.serviceType == "email".lower():
            # email()
            pass
        else:
            print(f"[x]- Invalid notification service of {self.serviceType} was provided.")
            return

        print(self.serviceType)
# NotificationWorker({"name": "morgan"}).rabbitMQCallback()
