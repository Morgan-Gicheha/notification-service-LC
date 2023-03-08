import requests

def sms( receiver:list, message:str,sender="LittleApp",):
    """_summary_

    Args:
        receiver (list): _description_
        message (str): _description_
        sender (str, optional): _description_. Defaults to "LittleApp".
    """
    url = "https://sms.little.bz/api/v1/message/"

    payload = {
        "from": "LittleApp",
        "to": list(receiver),
        "text": message
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer ZixokQ.Zsa2cLX6OsWrbh5lNkgOGX3Bth92oEVAfMhX"
    }

    try:
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.json())
    except Exception as e:
        # todo: try sending to craft.little.africa directly
        print("ERROR SENDING SMS")
        print(e)
        return