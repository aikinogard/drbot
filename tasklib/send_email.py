import logging
import json
import doctest
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def load_email_configure(path='email_configuration.json'):
    """load configuration json, it should be in the format
    {
        "sender": "senderXXX@gmail.com",
        "password": "senderpassword",
        "receivers": ["receiver1@gmail.com", "receiver2@gmail.com"]
    }

    >>> conf = load_email_configure(path='testlib/test_email_configuration.json')
    >>> conf['sender'] == 'senderXXX@gmail.com'
    True
    >>> conf['password'] == 'senderpassword'
    True
    >>> conf['receivers'] == 'receiver1@gmail.com, receiver2@gmail.com'
    True
    """
    with open(path, 'r') as f:
        js = json.load(f)
    if isinstance(js['receivers'], list):
        js['receivers'] = ', '.join(js['receivers'])
    return js

def send_email(subject, context, receivers, sender, password):
    """Need to allow "less secure apps" on your Gmail account.
    https://www.google.com/settings/security/lesssecureapps

    subject = 'this is the title'
    context = 'meow, meow'
    sender = 'xxx@gmail.com'
    password = 'xxx123'
    receivers = 'yyy@gmail.com' or 'yyy@gmail.com, zzz@gmail.com'
    """

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receivers
    msg['Subject'] = subject
    msg.attach(MIMEText(context, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        text = msg.as_string()
        server.sendmail(sender, receivers, text)
        server.quit()
        logging.info('mail sent to %s' % receivers)
        logging.info('subject %s' % subject)
        logging.info('context %s' % context)
    except smtplib.SMTPException as e:
        logging.error('fail to sent mail: %s' % e)

if __name__ == '__main__':
    doctest.testmod()