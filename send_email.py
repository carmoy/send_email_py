#!/usr/bin/python

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import sys

EMAIL_TITLE = 'Some Title'
SRC_EMAIL =  'source email address@gmail.com'
SRC_EMAIL_PASSWORD = 'some password'

MSG_BODY_TEMPLATE = 'This is a message body: \n {}'

def help():
  print 'Usage: '
  print 'send_main email mail_content'


def main(argv = None):
  if not argv or len(argv) != 3:
    help()
    sys.exit(1)

  toaddr = argv[1]
  msg = MIMEMultipart()
  msg['From'] = SRC_EMAIL
  msg['To'] = toaddr
  msg['Subject'] = EMAIL_TITLE

  body = MSG_BODY_TEMPLATE.format(argv[2])
  msg.attach(MIMEText(body, 'plain'))

  print 'login...'
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(SRC_EMAIL, SRC_EMAIL_PASSWORD)
  
  content_text = msg.as_string()
  server.sendmail(SRC_EMAIL, toaddr, content_text)
  print 'email sent to: ', toaddr
  print 'email: ', content_text
  sys.exit(0)

if __name__ == "__main__":
    main(argv = sys.argv)
