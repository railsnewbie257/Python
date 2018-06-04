# -*- coding: utf-8 -*-
import smtplib
gmail_user = "ppihokc@gmail.com"
gmail_pwd = "Pih2103a"
FROM = 'ppihokc@gmail.com'
TO = ['pihpj@oge.com'] #must be a list
SUBJECT = "Testing sending using gmail"
TEXT = "Test sending mail from the SAS server"
# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
  #server = smtplib.SMTP(SERVER) 
  server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
  server.ehlo()
  server.starttls()
  server.login(gmail_user, gmail_pwd)
  server.sendmail(FROM, TO, message)
  #server.quit()
  server.close()
  print ('successfully sent the mail')
except:
  print ("failed to send mail")
  
