import smtplib
import ssl
import time
from email.message import EmailMessage
import hashlib
import csv

def sendMail(subject,body):
    with open("mailPass.csv","r",newline="")as file:
        data=csv.reader(file)
        for i in data:
            sender=i[0]
            appPassword=i[1]

    msg=EmailMessage()
    msg["Subject"]=subject
    msg["From"]=sender
    msg["To"]=sender
    msg.set_content(body)

    try:
        context=ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context,timeout=10)as server:
            server.login(sender,appPassword)
            server.send_message(msg)
        print("Alert!!!File has been modyfied...Send Email sucessfully..")
    except (smtplib.SMTPException,OSError)as error:
        print("Process Failed:",error)
        

filePath="security.log"
def CalculateHash(filePath):
    Hash=hashlib.sha256()
    with open(filePath,"rb")as file:
        while True:
            data=file.read(4096)
            if not data:
                break
            Hash.update(data)
    HashVal=Hash.hexdigest()
    return HashVal
try:
    OrginalHash=CalculateHash(filePath)
    print("File Monitoring started..")
    while True:
        time.sleep(5)
        CurrentHash=CalculateHash(filePath)
        if OrginalHash != CurrentHash:
            sendMail(
                "Alert!!!","File has been modified.."
            )
            OrginalHash=CurrentHash
        else:
            print("File is unchanged")
            
except FileNotFoundError:
    print(f"File:{filePath} not found")
    
except KeyboardInterrupt:
    print("Monitoring Stoped")
    