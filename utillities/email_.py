import smtplib
from email.mime.text import MIMEText
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import dotenv_values

envVariable = dotenv_values(".env")


def processEmail(data: dict):
    availabeServices = ["mailgun", "pepipost"]

    if not "mailOptions" in data:
        data["mailOptions"] = {"service": "mailgun"}

    elif not "service" in data["mailOptions"]:
        data["mailOptions"]["service"] = "mailgun"
    elif not data["mailOptions"]["service"].lower() in availabeServices:
        data["mailOptions"]["service"] = "mailgun"

    if data["mailOptions"]["service"] == "mailgun":
        # calling mailgun
        sendUsingMailgun(data)

    if data["mailOptions"]["service"] == "pepipost":
        sendUsingPepipost()


def sendUsingMailgun(data: dict):

    # Mailgun SMTP credentials
    MAILGUN_SMTP_SERVER = envVariable["MAILGUN_SMTP_SERVER"]
    MAILGUN_SMTP_PORT = 587
    MAILGUN_SMTP_LOGIN = envVariable["MAILGUN_SMTP_LOGIN"]
    MAILGUN_SMTP_PASSWORD = envVariable["MAILGUN_SMTP_PASSWORD"]

    # Email content
    sender = data["from"]
    recipient = data["to"][0]

    try:
        subject = data["mailOptions"]["subject"]
    except:
        subject = ""

    msg = MIMEText(data["message"], "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        # Connect to Mailgun SMTP server
        server = smtplib.SMTP(MAILGUN_SMTP_SERVER, MAILGUN_SMTP_PORT)
        server.login(MAILGUN_SMTP_LOGIN, MAILGUN_SMTP_PASSWORD)

        # Send email
        server.sendmail(sender, recipient, msg.as_string())

        # Close the SMTP connection
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")


def sendUsingPepipost():
    print("calling Pepipost")
    pass
