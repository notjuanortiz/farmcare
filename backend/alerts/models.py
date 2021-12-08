import smtplib
from email.message import EmailMessage


class Alert():
    def __init__(self) -> None:
        self.msg = EmailMessage()
        self.msg['subject'] = "FarmCare Alert"
        self.msg['from'] = "ruhulsaad1971@gmail.com"
        self.user = "ruhulsaad1971@gmail.com"
        self.password = "kkxffitstckpjkbu"

    def send(self, receiver, body):
        self.msg['to'] = receiver
        self.msg.set_content(body)

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.user, self.password)
        server.send_message(self.msg)
        server.quit()
