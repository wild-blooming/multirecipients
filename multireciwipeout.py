import smtplib
from email.mime.text import MIMEText

import PyPDF2

import time


#smtp connection
smtpObj = smtplib.SMTP('SMTP server domain', 587)
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login('username', 'pwd')




#pdf extract
pdfFileObj = open('file.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
strEx = pdfReader.getPage(1).extractText()
strList = strEx.splitlines()
for i in reversed(range(len(strList))):
    if '@' in strList[i]: 
    
        SUBJECT = 'Subject'
        msg = ''
        TO = strList[i] 
        FROM = 'username'
        
        msg= MIMEText(msg)
        msg['Subject'] = SUBJECT
        msg['To'] = TO
        msg['From'] = FROM
#        print(TO) 
        smtpObj.sendmail(FROM, TO, msg.as_string())

    elif strList[i].find('Angela') != -1:
        break

    time.sleep(1)

smtpObj.quit()

