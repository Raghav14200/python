import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#username and password of the senders email
#use environment variables after learning it.
email="1ms19is096@gmail.com"
password="raghu@2001"

def send(text='Email Body',subject="Hi", to=None):
    if(isinstance(to,list)):
        msg=MIMEMultipart("alternative")
        msg["From"]="Raghavendra <1ms19is096@gmail.com>"
        msg['To']=', '.join(to)
        msg['Subject']=subject
        txt =MIMEText(text,'plain')
        msg.attach(txt)

        msg_str=msg.as_string()
        
        #login to smtp server
        server=smtplib.SMTP(host="smtp.gmail.com",port=587)
        server.ehlo()
        server.starttls()
        server.login(email,password)
        server.sendmail("Raghavendra <1ms19is096@gmail.com>",to,msg_str)
        server.quit()
