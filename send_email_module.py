import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import os
EMAIL_ADDRESS=os.environ['EMAIL_ADDRESS']
PASSWORD=os.environ['PASSWORD']

def send_email(to_email:str, content:str, subject:str, files:list):
    # email = EmailMessage()
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    part = MIMEApplication(
                files['file'],
                Name=files['name']
            )
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % files['name']
    msg.attach(part)
    msg.attach(MIMEText(content, "html"))
    # email["From"] = EMAIL_ADDRESS
    # email["To"] = to_email
    # email["Subject"] = "Correo de prueba"
    # email.set_content("Hola")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.local_hostname = 'lowercasehost'
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, PASSWORD)
    smtp.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
    smtp.quit()


# send_email("augustocarrillo20@gmail.com", "", "")"smtp-mail.outlook.com"