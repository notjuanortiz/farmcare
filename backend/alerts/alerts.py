import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
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
    
if __name__ == '__main__':
    # email_alert("Hey","Hello Word", "ananaziz98@gmail.com")
    email_alert("Hey","wine", "6234194111@tmomail.net")
    