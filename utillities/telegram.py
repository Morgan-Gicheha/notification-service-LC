import requests


def telegram(message: str, receiver: list = "Little_Alerts"):
    looped = 0
    """_summary_

    Args:
        message (str): _description_
        receiver (str, optional): _description_. Defaults to "Little_Alerts".
    """

    print("--->>>", receiver)
    print(len(receiver))
    if type(receiver) == list and len(receiver) > 1:
        list(map(lambda singleReceiver: telegram(message, singleReceiver), receiver))
        return
    elif type(receiver) == list and len(receiver) == 1:
        print(type(receiver))
        telegram(message, receiver[0])
        return


    url = "https://api.little.bz/internal/telegram/sendMessage"

    payload = {
        "group": receiver,
        "message": message
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)

    print("telegram response-->>>>>>>>>>>>>>>>", response.text)


