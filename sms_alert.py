

import smtplib
from email.message import EmailMessage
def sms_slert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['body']=body
    user="ajiet827@gmail.com"
    msg['from']=user
    password="phptylegmvudgqcw"
    server=smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()
if __name__=='__main__':
 sms_slert("hello","helloworld","likhithkulal0@gmail.com")