# Import smtplib for the actual sending function
import smtplib
import datetime
import hashlib

# Import the email modules we'll need
from email.mime.text import MIMEText


class SendEmailToMe:
    def __init__(self, sendersEmail, sendersName, messageText):

        #Making a substring for hashlib(md5) based on current date
        messageId = hashlib.md5(str(datetime.datetime.now())).hexdigest()[0:10]
        msg = MIMEText(messageText)
        me = sendersEmail
        you = 'oleg.ladizhensky@gmail.com'
        msg['Subject'] = 'ONBPM: '+sendersName+' send you a mail with Id: ' + messageId
        msg['From'] = sendersEmail
        msg['To'] = me


# Send the message via gmail. Change address and password accordingly to your settings.

        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo
        s.login('foo@gmail.com', 'yourpass')
        s.sendmail(me, [you], msg.as_string())
        s.quit()
        self.currentDatetime=messageId


