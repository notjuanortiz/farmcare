import smtplib
from email.message import EmailMessage
# import requests

def emailAlert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body) 
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = "ruhulsaad1971@gmail.com"
    
    user = "ruhulsaad1971@gmail.com"
    password = "kkxffitstckpjkbu"
    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    server.quit()
    
# if __name__ == '__main__':
    # emailAlert("Hey","Dont cheat", "xhajabx@gmail.com")
    # emailAlert("Hey","wine", "3475533214@tmomail.net")
    